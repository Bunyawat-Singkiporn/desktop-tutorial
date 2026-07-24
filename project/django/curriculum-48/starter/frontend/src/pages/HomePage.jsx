export default function HomePage() {
  return (
    <div className="space-y-3">
      <h1 className="text-2xl font-semibold">Starter frontend</h1>
      <p className="text-slate-600">
        React + Vite + Tailwind talking to Django at{" "}
        <code className="rounded bg-slate-100 px-1">http://127.0.0.1:8000</code>
      </p>
      <p className="text-sm text-slate-500">
        Open <strong>Tasks</strong> after the backend is running (
        <code>python manage.py runserver</code>).
      </p>
    </div>
  );
}
