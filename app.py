from flask import Flask, render_template, request, json
from stories import Story

app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route("/madlibs")
def madlib_input():
    '''Madlib input form'''
    return render_template("madlibs.html", prompts=story.prompts)


@app.route("/story")
def make_story():
    """Story filled out on page"""
    answers = {}
    for prompt in story.prompts:
        answers[prompt] = request.args[str(prompt)]
    end_story = story.generate(answers)
    return render_template("story.html", end_story=end_story)
