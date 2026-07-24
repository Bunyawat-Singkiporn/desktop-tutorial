# S20 — Search, ordering, pagination

## Goal

Add search + ordering + page size to the list API and UI.

## Concept (5 min)

DRF: SearchFilter, OrderingFilter, PageNumberPagination
Frontend: search box + next/prev

## Backend steps

- Configure filter_backends and pagination_class
- Test ?search=&ordering=&page=

## Frontend steps

- Search input debounced or on submit
- Prev/Next using page links from response

## Check

- [ ] Search finds by title
- [ ] Page 2 works when enough rows

## Common bugs

- Ignoring paginated response shape { count, results }
