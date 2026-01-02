# Contributing to Wolof NLP

Thank you for your interest in contributing to Wolof NLP! This project aims to build high-quality NLP tools for the Wolof language, and we welcome contributions from everyone.

## Ways to Contribute

### 1. Report Bugs

If you find a bug, please open an issue with:
- A clear description of the problem
- Steps to reproduce the issue
- Expected vs actual behavior
- Example text that causes the issue

### 2. Suggest Enhancements

Have an idea for improvement? Open an issue describing:
- The enhancement you'd like to see
- Why it would be useful
- Any implementation ideas you have

### 3. Improve the Lexicon

Help us expand the Wolof vocabulary in `constants.py`:
- Add missing common words
- Add domain-specific vocabulary
- Correct any errors in existing entries

### 4. Add Test Cases

More test cases help ensure quality:
- Add examples to `gold_standard.json`
- Include edge cases you've encountered
- Cover code-switching scenarios

### 5. Improve Documentation

Documentation in multiple languages is especially valuable:
- Add code examples
- Improve API documentation

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/maimouna-mbacke/wolof-nlp.git
   cd wolof-nlp
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

4. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

5. Run tests:
   ```bash
   pytest
   ```

## Pull Request Process

1. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Open a Pull Request with:
   - Clear description of changes
   - Any related issue numbers
   - Test results if applicable

## Code Style

- Follow PEP 8 guidelines
- Use type hints where possible
- Add docstrings for public functions
- Keep functions focused and small

## Commit Messages

Use clear, descriptive commit messages:
- `Add: new feature description`
- `Fix: bug description`
- `Update: what was updated`
- `Docs: documentation changes`

## Questions?

Feel free to open an issue for any questions about contributing.

---

**Jërejëf!** (Thank you!)
