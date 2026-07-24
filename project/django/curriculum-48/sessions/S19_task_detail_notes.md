# S19 — Task detail with related notes

## Goal

Show one task and nested related notes.

## Concept (5 min)

1:N Task -> Notes
Serializer can nest NoteSerializer(many=True, read_only=True)

## Backend steps

- Note model with FK to Task
- Nested serializer on detail
- Optional: POST /api/tasks/1/notes/

## Frontend steps

- Detail route /tasks/:id
- Render task fields + notes list

## Check

- [ ] Detail shows nested notes
- [ ] 404 for missing id

## Common bugs

- N+1 queries — ok for class size; mention select_related later
