def truncate_text(text, max_length=100):
    if len(text) > max_length:
        return f'{text[:max_length]}...'
    return text
