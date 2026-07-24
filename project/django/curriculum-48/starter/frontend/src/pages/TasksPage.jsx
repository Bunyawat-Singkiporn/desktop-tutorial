import { useEffect, useState } from "react";
import { apiFetch } from "../api/client.js";

export default function TasksPage() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  async function load() {
    setLoading(true);
    setError("");
    try {
      const data = await apiFetch("/api/tasks/");
      setTasks(Array.isArray(data) ? data : data.results || []);
    } catch (e) {
      setError(e.data ? JSON.stringify(e.data) : e.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();
  }, []);

  async function onCreate(e) {
    e.preventDefault();
    setError("");
    try {
      await apiFetch("/api/tasks/", {
        method: "POST",
        body: JSON.stringify({ title, done: false }),
      });
      setTitle("");
      await load();
    } catch (err) {
      setError(err.data ? JSON.stringify(err.data) : err.message);
    }
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Tasks</h1>

      <form onSubmit={onCreate} className="flex flex-wrap gap-2">
        <input
          className="min-w-[16rem] flex-1 rounded border border-slate-300 px-3 py-2"
          placeholder="New task title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <button
          type="submit"
          className="rounded bg-slate-900 px-4 py-2 text-white hover:bg-slate-700"
        >
          Add
        </button>
      </form>

      {error && (
        <p className="rounded border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-700">
          {error}
        </p>
      )}

      {loading ? (
        <p className="text-slate-500">Loading…</p>
      ) : tasks.length === 0 ? (
        <p className="text-slate-500">No tasks yet — add one or create rows in Admin.</p>
      ) : (
        <table className="w-full border-collapse text-left text-sm">
          <thead>
            <tr className="border-b border-slate-200 text-slate-500">
              <th className="py-2 pr-4">ID</th>
              <th className="py-2 pr-4">Title</th>
              <th className="py-2">Done</th>
            </tr>
          </thead>
          <tbody>
            {tasks.map((t) => (
              <tr key={t.id} className="border-b border-slate-100">
                <td className="py-2 pr-4">{t.id}</td>
                <td className="py-2 pr-4">{t.title}</td>
                <td className="py-2">{t.done ? "yes" : "no"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
