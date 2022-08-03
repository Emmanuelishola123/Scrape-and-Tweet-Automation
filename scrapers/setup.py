
def format_description_text(description):
    if len(description) > 150:
        if len(description.split('.')[0]) > 150 or len(description.split('?')[0]) > 150 or len(description.split('!')[0]) > 150:
            return description[:145] + '...' 
        return description.split('.')[0] or description.split('?')[0] or description.split('!')[0]
    else:
         return description