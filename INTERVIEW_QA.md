# myProfile — interview questions and answers

[README](README.md) · [Project architecture](PROJECT_ARCHITECTURE.md)

Answers below use this repository’s files and implementation. They distinguish existing behavior from suggested extensions; source links let you verify each walkthrough.

## 1. What problem does myProfile address, and what can you demonstrate?

A Streamlit portfolio combining DevOps experience, poetry, interactive visualizations, AI assistance, and content administration.

I would demonstrate the linked implementation or examples and distinguish that evidence from any planned production features. Start with [`README.md`](README.md).

## 2. How is this repository organized?

- [`components/skills_visualization.py`](components/skills_visualization.py): Implementation or supporting configuration.
- [`components/poetry_section.py`](components/poetry_section.py): Implementation or supporting configuration.
- [`components/contact_info.py`](components/contact_info.py): Implementation or supporting configuration.
- [`app.py`](app.py): Implementation or supporting configuration.
- [`components/career_timeline.py`](components/career_timeline.py): Implementation or supporting configuration.
- [`backend/admin_panel.py`](backend/admin_panel.py): Implementation or supporting configuration.
- [`admin.py`](admin.py): Implementation or supporting configuration.
- [`ai_assistant.py`](ai_assistant.py): Implementation or supporting configuration.

[PROJECT_ARCHITECTURE.md](PROJECT_ARCHITECTURE.md) contains the component diagram and the implementation walkthrough.

## 3. Can you walk through `render_skills_visualization` and explain the decision it makes?

The main walkthrough here is `render_skills_visualization(skills_data)` in [`components/skills_visualization.py`](components/skills_visualization.py#L6). Render interactive skills visualization

```python
def render_skills_visualization(skills_data):
    """Render interactive skills visualization"""
    
    # Skills overview
    tab1, tab2, tab3 = st.tabs(["📊 Skills Overview", "🎯 Proficiency Levels", "📈 Skills Comparison"])
    
    with tab1:
        # Create a comprehensive skills dataframe
        all_skills = []
        for category, skills in skills_data.items():
            for skill, proficiency in skills.items():
                all_skills.append({
                    'Category': category,
                    'Skill': skill,
                    'Proficiency': proficiency
                })
        
        skills_df = pd.DataFrame(all_skills)
        
        # Sunburst chart for skills hierarchy
```

This is an excerpt; follow the source link for the rest of the branches.

The implementation calls `all_skills.append`, `all_skills_flat.append`, `category_skills.keys`, `category_skills.values`, `dict`, `enumerate`, `fig_bar.update_layout`, `fig_radar.add_trace`, `fig_radar.update_layout`. In an interview, trace those calls in execution order using a fixture input.

## 4. What responsibility does `render_poetry_section` have?

`render_poetry_section(poetry_content)` is defined in [`components/poetry_section.py`](components/poetry_section.py#L4). Render the poetry and creative passion section

It uses `datetime.datetime.now`, `enumerate`, `len`, `random.choice`, `st.button`, `st.columns`, `st.expander`, `st.info`. This is the code path I would compare against the caller to explain responsibility boundaries.

## 5. What would you verify before extending this repository?

I would identify an executable example or define a concrete acceptance case for the material in [`README.md`](README.md). For code, verify inputs, outputs, and failure handling; for notes or templates, verify that a reader can follow the procedure and distinguish examples from measured results.

## 6. How would you verify correctness when no test suite is present?

There are no dedicated test files in the inspected first-party inventory. I would select one concrete example from [`README.md`](README.md), define expected output or an acceptance checklist, and add repeatable verification before expanding scope. For a documentation-only repository, that means checking links, instructions, and the reproducibility of examples.

## 7. How do you separate the current design from a future production design?

The current design is the source/component map in [PROJECT_ARCHITECTURE.md](PROJECT_ARCHITECTURE.md). A future deployment needs explicit input contracts, persistence decisions, authentication, monitoring, and rollback. I would present these as proposed work until the corresponding implementation and verification exist.

## 8. Where does state live, and what happens with multiple workers?

Module-level containers include `insights` in [`ai_assistant.py`](ai_assistant.py); `CERTIFICATIONS`, `CERTIFICATION_CATEGORIES`, `CERTIFICATION_STATS` in [`data/certifications.py`](data/certifications.py); `POETRY_CONTENT` in [`data/poetry_content.py`](data/poetry_content.py); `SKILLS_DATA`, `CERTIFICATIONS`, `CORE_COMPETENCIES` in [`data/skills_data.py`](data/skills_data.py).

These containers belong to a Python process. Inspect which are constant fixtures and which are mutated. Mutable process state needs an explicit shared-storage or synchronization strategy before multiple workers can provide consistent behavior.

## 9. How would another engineer reproduce your walkthrough?

Follow [`README.md`](README.md) and the linked component documents. This documentation update does not assert an application launch command for a repository without a verified launch contract.

## 10. How would you add CI without confusing it with deployment?

First automate the repository-specific checks above, including documentation link validation. Add deployment only after defining the target environment, required credentials, approval boundary, smoke test, and rollback procedure. No GitHub Actions workflow is asserted by the inspected inventory.

## 11. How would you present this project in a Forward Deployed Engineer interview?

Start with the user and operational problem described in [`README.md`](README.md). Explain one constraint that changes the implementation, show the linked code or example, and walk through a success case and a failure case. Agree on a measurable acceptance criterion before expanding the solution, and leave a handoff with data boundaries and rollback ownership. Any proposed production or business metric should be identified as a target until measured.

## 12. What is the input-to-output contract of `render_skills_visualization`?

In [`components/skills_visualization.py`](components/skills_visualization.py#L6), `render_skills_visualization(skills_data)` receives the inputs. The function computes these intermediate values:

- `tab1, tab2, tab3 = st.tabs(['📊 Skills Overview', '🎯 Proficiency Levels', '📈 Skills Comparison'])`

## 13. Which decision rules or boundary conditions should an interviewer challenge?

The implementation in [`components/skills_visualization.py`](components/skills_visualization.py#L6) branches on:

- `selected_category == 'Cloud Platforms'`
- `selected_category == 'DevOps & CI/CD'`
- `i < 5`
- `selected_category == 'Containerization'`
- `selected_category == 'Programming Languages'`
- `selected_category == 'MLOps Tools'`

A useful extension is a table-driven test that covers each condition just below, at, and above its boundary where applicable. These expressions are the current rules; changing them changes behavior and should be justified by the project’s acceptance criteria.
