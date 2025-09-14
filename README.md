# Unified Compliance UI

## 1) What this is for

A single Streamlit app to kick off and track **three OSS/compliance workflows** in your repo—without jumping between different UIs:

* **FOSSology**: license scanning with official reports (SPDX2, ReadmeOSS, License Text/List).
* **ScanCode Toolkit**: licenses/copyright/packages + optional SBOMs (CycloneDX, SPDX).
* **SCANOSS**: component/license discovery with JSON + Excel summaries.

It standardizes:

* Inputs: **docker**, **repo**, **upload-zip**, **upload-tar**
* Ref selection: **Load Tags / Load Branches** for GitHub repos
* Output naming: shows the **predicted filename tag** so artifacts are easy to find
* One place to **dispatch** workflows, see **status**, open the **run**, and **download artifacts**

---

## 2) How it’s built

* **Framework**: Streamlit (no sidebar; all controls in the main view).
* **APIs used** (GitHub REST):

  * Dispatch: `POST /repos/{owner}/{repo}/actions/workflows/{file}/dispatches`
  * Runs: `GET /repos/{owner}/{repo}/actions/workflows/{file}/runs`
  * Run details: `GET /repos/{owner}/{repo}/actions/runs/{run_id}`
  * Artifacts: `GET /repos/{owner}/{repo}/actions/runs/{run_id}/artifacts`
  * (Optional) Upload file to repo for a shareable URL: `PUT /repos/{owner}/{repo}/contents/{path}`
* **Config in code**:

  ```python
  OWNER  = "<org-or-user>"
  REPO   = "<repo>"
  BRANCH = "main"
  WF_FOSSOLOGY = "fossology_final.yml"
  WF_SCANCODE  = "scancode_workflow.yml"
  WF_SCANOSS   = "scanoss_workflow.yml"
  ```
* **Auth**: place a token in `.streamlit/secrets.toml`

  ```toml
  GITHUB_TOKEN = "ghp_xxx..."
  ```

  Recommended scopes:

  * `actions:read` (list/download artifacts via API)
  * `workflow:write` (dispatch workflows)
  * `contents:write` (only if you use “Upload file to repo” from the UI)
* **UX details**:

  * **Load Tags / Load Branches** appear only in **repo** mode and use GitHub’s refs endpoints.
  * Uses `st.query_params` (not the deprecated experimental API) for auto-refresh.
  * Timestamps are handled as **timezone-aware** to avoid comparison errors.
  * Values sent by the UI **must match workflow `options` exactly** (e.g., `upload-tar`), or GitHub returns **422**.

---

## 3) How to use

1. **Pick a tool**
   Choose **FOSSology**, **ScanCode Toolkit**, or **SCANOSS**. The form below adapts to that workflow’s inputs.

2. **Choose input & options**

* **Scan Type**: `docker` | `repo` | `upload-zip` | `upload-tar`

  * **docker**: enter image (e.g., `eclipse-temurin:17-jre-alpine`)
  * **repo**: paste GitHub URL (`.git` or a web URL like `/tree/v1.2.3`), enter ref if needed
    • Click **🔖 Load Tags** / **🌿 Load Branches** → select → **Use Tag/Branch**
  * **upload-zip/tar**: paste a **direct file URL**, or **upload** a file and let the UI push it into `uploads/<ts>/` in your repo (it auto-fills the URL)
* Review the **Expected filename tag** preview (this suffix appears in artifact/report names).
* Set tool-specific toggles:

  * **FOSSology**: `nomos`, `ojo`, `monk`, `copyright` (defaults ON; `ojo` implies `nomos`)
  * **ScanCode**: enable `license`, `copyright`,
    `package`, and optional `SBOM export`
  * **SCANOSS**: enable scan; pick image scan mode per your YAML (manual/syft)

3. **Dispatch**
   Click **▶️ Run Scan**. The UI stores a timestamp and then fetches the latest run created after that moment.

4. **Track & download**

* See **Run link**, **status/conclusion**, **created/updated** times.
* Toggle **Auto-refresh** to keep the view live.
* When ready, **Artifacts** are listed (name + size).

  * If clicking an artifact API link shows **403** (“actions scope required”), download from the run’s **Artifacts** panel or use a token with `actions:read`.

**Quick tips / fixes**

* **422 “value not in allowed values”** → UI choice must match the workflow `options` exactly.
* **No run found yet** → give it a few seconds; enable **Auto-refresh**.
* **Empty results** → verify repo ref, ensure upload URL is a **direct download**, and confirm docker image exists.
* **Load Tags empty** → token must access the repo and the URL must be a GitHub repo; otherwise select the ref manually.
