import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os


def run_gui(process_function):
    def select_pdf():
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            pdf_path_var.set(file_path)
            update_output_path(file_path)

    def update_output_path(input_path):
        if input_path:
            directory = os.path.dirname(input_path)
            filename = os.path.splitext(os.path.basename(input_path))[0] + "_masked.pdf"
            output_path = os.path.join(directory, filename)
            output_path_var.set(output_path)

    def select_destination():
        initial_dir = os.path.dirname(output_path_var.get()) if output_path_var.get() else "/"
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialdir=initial_dir,
            initialfile=os.path.basename(output_path_var.get())
        )
        if file_path:
            output_path_var.set(file_path)

    def mask_pdf():
        pdf_path = pdf_path_var.get()
        output_pdf_path = output_path_var.get()
        selected_language_name = language_var.get()

        # Convert the selected language name to its corresponding code
        selected_language_code = next(lang[1] for lang in languages if lang[0] == selected_language_name)

        if not pdf_path or not output_pdf_path:
            messagebox.showerror("Error", "Please select both input and output files.")
            return

        progress_bar['value'] = 0
        root.update_idletasks()

        try:
            def update_progress(value):
                progress_bar['value'] = value
                root.update_idletasks()

            process_function(pdf_path, output_pdf_path, update_progress, selected_language_code)

            messagebox.showinfo("Success", f"File saved as {output_pdf_path}")
            root.quit()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            progress_bar['value'] = 0

    # Initialize the main window
    root = tk.Tk()
    root.title("PDF Masking Tool")
    root.geometry("600x350")
    root.configure(bg='#f0f0f0')

    style = ttk.Style()
    style.theme_use('clam')

    main_frame = ttk.Frame(root, padding="20 20 20 20")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Variables
    pdf_path_var = tk.StringVar()
    output_path_var = tk.StringVar()
    language_var = tk.StringVar(value="English")  # Default to English

    # Input PDF selection
    ttk.Label(main_frame, text="Input PDF:").grid(column=0, row=0, sticky=tk.W, pady=5)
    ttk.Entry(main_frame, width=50, textvariable=pdf_path_var).grid(column=0, row=1, sticky=(tk.W, tk.E), pady=5)
    ttk.Button(main_frame, text="Browse", command=select_pdf).grid(column=1, row=1, sticky=tk.W, padx=(5, 0), pady=5)

    # Output PDF selection
    ttk.Label(main_frame, text="Output PDF:").grid(column=0, row=2, sticky=tk.W, pady=5)
    ttk.Entry(main_frame, width=50, textvariable=output_path_var).grid(column=0, row=3, sticky=(tk.W, tk.E), pady=5)
    ttk.Button(main_frame, text="Browse", command=select_destination).grid(column=1, row=3, sticky=tk.W, padx=(5, 0),
                                                                           pady=5)

    # Language selection
    ttk.Label(main_frame, text="PDF Language:").grid(column=0, row=4, sticky=tk.W, pady=5)
    languages = [
        ("English", "eng"),
        ("Spanish", "spa"),
        ("French", "fra"),
        ("German", "deu"),
        ("Italian", "ita"),
        ("Hindi", "hin"),
        ("Korean", "kor"),
        ("Russian", "rus"),
        ("Chinese (Simplified)", "chi_sim"),
        ("Malay", "msa"),
        ("Japanese", "jpn")
    ]
    language_dropdown = ttk.Combobox(main_frame, textvariable=language_var,
                                     values=[lang[0] for lang in languages], state="readonly")
    language_dropdown.grid(column=0, row=5, sticky=(tk.W, tk.E), pady=5)
    language_dropdown.current(0)  # Set default to English

    # Progress Bar
    progress_bar = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
    progress_bar.grid(column=0, row=6, columnspan=2, sticky=(tk.W, tk.E), pady=20)

    # Mask PDF Button
    mask_button = ttk.Button(main_frame, text="Mask PDF", command=mask_pdf)
    mask_button.grid(column=0, row=7, columnspan=2, pady=10)

    # Configure grid
    main_frame.columnconfigure(0, weight=1)
    for i in range(8):
        main_frame.rowconfigure(i, weight=1)

    # Start the GUI event loop
    root.mainloop()