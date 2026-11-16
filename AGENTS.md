# Team project documentation

Project code: PRJ_070_ST044_ST009_ST040  
Team members: ST044, ST009, ST040

This repository contains shared STHDF course documentation generated from the class template.

## Main content

Our documentation root is:
`content/docs/sk/sthdf/PRJ_070_ST044_ST009_ST040/`

- `projects/index.md`: project documentation entry point.
- `projects/7ds/`: management, goals, plans, decisions, and lessons learned.
- `projects/q12/`: project value and lifecycle documentation.
- `projects/sdlc/`: requirements, analysis, design, implementation, testing, deployment, and maintenance.
- `students/`: generated submission sections. Keep personal reflection and individual contributions clearly attributed.
- `core/`: shared generators and templates.
- `config/`: generator configuration.
- `publishing/docusaurus/`: documentation website tooling.

## Working rules

- Follow the existing generated structure and Markdown conventions.
- Preserve YAML front matter, identifiers, and navigation unless a change requires updating them.
- Use relative links for documents and assets within this repository.
- Keep project-specific changes within our documentation root where practical.
- Update navigation when adding or moving pages, and verify affected local links.
- Do not invent requirements, completed work, test results, dates, or individual contributions. Mark missing information as TODO.
- Distinguish implemented functionality from planned or experimental functionality.
- Preserve the document's existing language unless asked to translate it.
- Avoid changing shared generators, templates, or publishing configuration for routine documentation tasks.
- Do not regenerate existing content with EXISTS=replace during ordinary editing.

## Setup

Run commands from the repository root in WSL.

The initial documentation generation command is:
`make S31-sthdf-new STHDF_NAME=PRJ_070_ST044_ST009_ST040 STHDF_TITLE="PRJ_070_ST044_ST009_ST040" LOCALE=sk EXISTS=error`

Generation is a setup step, not a routine editing step.
