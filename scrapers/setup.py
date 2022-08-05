
def format_description_text(description):
    if len(description) > 135:
        if len(description.split('.')[0]) > 135 or len(description.split('?')[0]) > 135 or len(description.split('!')[0]) > 135:
            return description[:130] + '...' 
        return description.split('.')[0] or description.split('?')[0] or description.split('!')[0]
    else:
         return description