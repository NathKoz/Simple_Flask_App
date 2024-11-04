from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionaries for each language with code examples
code_examples = {
    "python": {
        "print": "print('Hello, World!')",
        "input": "name = input('Enter your name: ')\nprint(f'Hello, {name}!')",
        "loop": "for i in range(5):\n    print(i)",
    },
    "csharp": {
        "print": "Console.WriteLine(\"Hello, World!\");",
        "input": "Console.Write(\"Enter your name: \");\nstring name = Console.ReadLine();\nConsole.WriteLine($\"Hello, {name}!\");",
        "loop": "for (int i = 0; i < 5; i++) {\n    Console.WriteLine(i);\n}",
    },
    "rust": {
        "print": "println!(\"Hello, World!\");",
        "input": "use std::io;\nlet mut name = String::new();\nio::stdin().read_line(&mut name).expect(\"Failed to read line\");\nprintln!(\"Hello, {}!\", name.trim());",
        "loop": "for i in 0..5 {\n    println!(\"{}\", i);\n}",
    },
}

@app.route("/", methods=["GET", "POST"])
def index():
    example_code = None
    selected_language = "python"  # Default language
    selected_keyword = None

    if request.method == "POST":
        selected_language = request.form.get("language")
        selected_keyword = request.form.get("keyword")
        example_code = code_examples.get(selected_language, {}).get(selected_keyword, "No example available.")

    return render_template(
        "index.html",
        example_code=example_code,
        selected_language=selected_language,
        selected_keyword=selected_keyword,
    )

if __name__ == "__main__":
    app.run(debug=True)
