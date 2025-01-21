# Task Tracker CLI

Task Tracker CLI is a simple command-line application for managing tasks. It allows you to add, update, delete, and track the status of your tasks using the terminal. Tasks are stored in a JSON file, making it easy to persist and retrieve them.

<https://roadmap.sh/projects/task-tracker>

---

## Features

- **Add Tasks**: Add new tasks with a description.
- **Update Tasks**: Modify the description of an existing task.
- **Delete Tasks**: Remove a task by its unique ID.
- **Change Status**: Mark tasks as `todo`, `in-progress`, or `done`.
- **List Tasks**: View all tasks or filter tasks by status, displayed in a tabular format.
- **JSON Storage**: Tasks are saved in a `tasks.json` file in the current directory.

---

## Requirements

- Python 3.6 or higher
- `tabulate` framework (Install using `pip install tabulate`)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nerdifydev/TaskTrackerCLI.git
   ```

2. Navigate to the project directory:

   ```bash
   cd TaskTrackerCLI
   ```

3. Install the required dependencies:

   ```bash
   pip install tabulate
   ```

4. Run the application:

   ```bash
   python3 main.py --help
   ```

---

## Usage

### Add a Task

```bash
python3 main.py add "Task description"
```

### Update a Task

```bash
python3 main.py update <id> "Updated description"
```

### Delete a Task

```bash
python3 main.py delete <id>
```

### Mark Task as In-Progress or Done

- Mark as In-Progress:

  ```bash
  python3 main.py mark-in-progress <id>
  ```

- Mark as Done:

  ```bash
  python3 main.py mark-done <id>
  ```

### List Tasks

- List all tasks:

  ```bash
  python3 main.py list
  ```

- List tasks by status:

  ```bash
  python3 main.py list -s <todo|in-progress|done>
  ```

---

## Examples

1. **Add a Task**:

   ```bash
   python3 main.py add "Complete Python project"
   ```

2. **Update a Task**:

   ```bash
   python3 main.py update 1 "Complete Python CLI project"
   ```

3. **Mark as In-Progress**:

   ```bash
   python3 main.py mark-in-progress 1
   ```

4. **Mark as Done**:

   ```bash
   python3 main.py mark-done 1
   ```

5. **List All Tasks**:

   ```bash
   python3 main.py list
   ```

6. **List In-Progress Tasks**:

   ```bash
   python3 main.py list -s in-progress
   ```

7. **Delete a Task**:

   ```bash
   python3 main.py delete 1
   ```

---

## File Structure

- **`tasks.json`**: Stores task data in the following format:

```json
[
    {
        "id": 1,
        "description": "Complete Python project",
        "status": "todo",
        "createdAt": "2025-01-20T12:00:00",
        "updatedAt": "2025-01-20T12:00:00"
    }
]
```

---

## Error Handling

- Provides user-friendly error messages for invalid inputs.
- Gracefully handles missing or malformed `tasks.json` files.

---

## License

This project is open-source and available under the MIT License.
