from questions.models import Tag

tags = {
    'root':{
        'science': {
            'physics': {
                'electricity':'',
                'magnetism': '',
                'motion': '',
            },
            'chemistry': {
                'organic': '',
                'inorganic': '',
                'physical': '',
            },
            'biology': {
                'microbiology': '',
                'cell theory': '',
            },
            'mathematics': {
                'geometry': '',
                'calculus': {
                    'differentiation': '',
                    'integration': '',
                },
                'linear algebra': '',
                'trigonometry': '',
                'statistics': {
                    'probability': '',
                },
            },
        },
        'humanities': {
            'anthropology': '',
            'archeology': '',
            'economics': '',
            'geography': '',
            'history': '',
            'law': '',
            'psychology': '',
            'sociology': '',
        }
    }
}

def parse_tags(dick, parent):
    if not dick: return
    for tag in dick.keys():
        print(tag, parent)
        obj = Tag.objects.create(name=tag, parent=parent)
        parse_tags(dick[tag], obj)

if __name__=='__main__':
    parse_tags(tags['root'], Tag.objects.get_or_create(name='root'))
