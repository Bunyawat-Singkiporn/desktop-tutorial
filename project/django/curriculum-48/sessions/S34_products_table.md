# S34 — Products table + image URL + filter by category

## Goal

List products with category filter.

## Concept (5 min)

image_url as URLField/CharField for class simplicity (no media upload yet).

## Backend steps

- Product + Category models + APIs
- Filter ?category=

## Frontend steps

- Products table page
- Thumbnail from image_url
- Category filter

## Check

- [ ] Table loads
- [ ] Filter works

## Common bugs

- Broken image URLs — use placeholder
