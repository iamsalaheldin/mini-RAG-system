# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A minimal RAG (Retrieval-Augmented Generation) implementation for question answering, built with FastAPI. The project is currently being reorganized into a `src/` layout (old top-level `main.py`, `routes/`, `requirements.txt` are staged for deletion and replaced by equivalents under `src/`).

## Environment Setup

Uses Python 3.13 via Conda:
```bash
conda create -n mini-rag python=3.13
conda activate mini-rag
pip install -r src/requirements.txt
cp .env.example .env  # then fill in OPENAI_API_KEY
```

Required `.env` variables: `APP_NAME`, `APP_VERSION`, `OPENAI_API_KEY`

## Running the Server

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
```

## Architecture

- **Entry point**: `src/main.py` — creates the FastAPI app, loads `.env`, mounts routers
- **Routing**: `src/routes/` — each router uses `APIRouter` with prefix `/api/v1`; routers are imported using relative imports (e.g. `from .routes import base`) and registered in `main.py`
- **Assets**: `src/assets/mini-rag-app.postman_collection.json` — Postman collection for API testing

New routes should be added as separate files under `src/routes/`, following the pattern in [src/routes/base.py](src/routes/base.py), and registered in `src/main.py`.
