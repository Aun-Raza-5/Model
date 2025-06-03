import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load saved model and data
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)
with open("feature_names.pkl", "rb") as f:
    feature_names = pickle.load(f)

# Define question structure
questions = [
    ("🧠 Does your child have trouble understanding body language or facial expressions?", "A9_Score"),
    ("🗣️ Does your child struggle to start conversations or social interactions?", "A4_Score"),
    ("🔊 Is your child overly sensitive to sounds, lights, or textures?", "A6_Score"),
    ("👂 Does your child fail to respond when their name is called?", "A3_Score"),
    ("👤 What is your relation to the child?", "relation"),
    ("🧸 Does your child prefer to play alone rather than with others?", "A2_Score"),
    ("🔁 Does your child repeat words or phrases?", "A10_Score"),
    ("🌍 What is your child's ethnicity?", "ethnicity"),
    ("👀 Does your child look at you when you call their name?", "A1_Score"),
    ("🏠 What is your country of residence?", "contry_of_res"),
    ("🎂 Age of your child?", "age"),
    ("🚻 Gender of your child?", "gender"),
    ("☀️ Did your child have jaundice at birth?", "jaundice"),
    ("👁️‍🗨️ Does your child struggle with eye contact?", "A5_Score"),
    ("🔄 Does your child have strong reactions to changes in routine?", "A8_Score"),
    ("👉 Does your child use gestures (like pointing)?", "A7_Score"),
    ("🧩 Has your child been previously diagnosed with autism?", "austim"),
    ("📱 Have you used this screening tool before?", "used_app_before")
]

# Important features (top ranked)
important_fields = ["A9_Score", "A4_Score", "A6_Score", "A3_Score", "relation", "A2_Score"]

# Window setup
root = tk.Tk()
root.title("🧠 Autism Spectrum Disorder (ASD) Predictor")
root.configure(bg="#f2f6ff")
root.geometry("700x600")

bg_color = "#f2f6ff"
accent_color = "#b3d1ff"
label_font = ("Helvetica", 11)
entry_font = ("Helvetica", 11)

# Canvas and scrollbar setup
canvas = tk.Canvas(root, bg=bg_color, highlightthickness=0)
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
form_frame = tk.Frame(canvas, bg=bg_color)

canvas_frame = canvas.create_window((0, 0), window=form_frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

# Scroll configuration
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
form_frame.bind("<Configure>", on_frame_configure)

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Inputs storage
inputs = {}

# Add input widgets with improved layout
for i, (question, field) in enumerate(questions):
    number = f"{i+1}."
    prefix = f"{number} "
    if field in important_fields:
        prefix = f"⭐ {number} "

    label_text = prefix + question

    tk.Label(form_frame, text=label_text, wraplength=400, justify="left",
             font=("Helvetica", 11, "bold") if field in important_fields else label_font,
             bg=bg_color).grid(row=i, column=0, sticky="w", padx=15, pady=6)

    if field == "age":
        entry = tk.Entry(form_frame, font=entry_font)
        entry.grid(row=i, column=1, padx=10, pady=4)
        inputs[field] = entry
    elif field in encoders:
        var = tk.StringVar()
        cb = ttk.Combobox(form_frame, textvariable=var, values=list(encoders[field].classes_),
                          state="readonly", font=entry_font)
        cb.set(encoders[field].classes_[0])
        cb.grid(row=i, column=1, padx=10, pady=4)
        inputs[field] = var
    else:
        var = tk.StringVar()
        cb = ttk.Combobox(form_frame, textvariable=var, values=["Yes", "No"],
                          state="readonly", font=entry_font, width=10)
        cb.set("No")
        cb.grid(row=i, column=1, padx=10, pady=4)
        inputs[field] = var

# Predict button and logic
def predict():
    try:
        data = {}
        for _, field in questions:
            val = inputs[field].get()
            if field == "age":
                data[field] = float(val)
            elif field in encoders:
                data[field] = val
            else:
                data[field] = 1 if val == "Yes" else 0

        df = pd.DataFrame([data])
        for col in df.select_dtypes(include="object").columns:
            if col in encoders:
                df[col] = encoders[col].transform(df[col])

        features_only = [col for col in feature_names if col != "Class/ASD"]
        df = df[features_only]

        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]
        label = "🧠 ASD" if pred == 1 else "✅ Non-ASD"

        # Show result window
        result_win = tk.Toplevel(root)
        result_win.title("Prediction Result")
        result_win.configure(bg="white")
        result_win.geometry("420x380")

        tk.Label(result_win, text=f"Prediction: {label}", font=("Helvetica", 16, "bold"), fg="blue", bg="white").pack(pady=10)
        tk.Label(result_win, text=f"Probability of ASD: {prob:.2f}", font=("Helvetica", 14), bg="white").pack()

        # Create chart
        fig, ax = plt.subplots(figsize=(3, 2.5))
        ax.bar(["Non-ASD", "ASD"], [1 - prob, prob], color=["green", "red"])
        ax.set_ylim(0, 1)
        ax.set_ylabel("Probability")
        ax.set_title("Prediction Confidence")

        # Embed chart in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=result_win)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

    except Exception as e:
        messagebox.showerror("Error", f"Prediction failed:\n{str(e)}")

# Predict Button
tk.Button(form_frame, text="🔍 Predict", command=predict, bg=accent_color,
          font=("Helvetica", 13, "bold"), fg="black", width=20).grid(row=len(questions), columnspan=2, pady=30)

root.mainloop()
