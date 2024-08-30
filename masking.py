import fitz

def mask_text_in_pdf(input_pdf, output_pdf, target_texts, mask_char=' '):
    doc = fitz.open(input_pdf)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        for target_text in target_texts:
            text_instances = page.search_for(target_text)

            for inst in text_instances:
                page.add_redact_annot(inst, fill=(0, 0, 0))

                page.apply_redactions()

                rect = inst
                text = mask_char * len(target_text)
                page.insert_text((rect.x0, rect.y1 - 2), text, fontname="helv", fontsize=((rect.y1 - rect.y0) - 3),
                                 color=(0, 0, 0))

    doc.save(output_pdf)