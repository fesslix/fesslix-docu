import pybtex.plugin
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.richtext import Tag, Text, Protected
from pybtex.style.template import sentence, field, href, words
from pybtex.style.formatting import FormattedEntry

class MyStyle(UnsrtStyle):
    def format_title(self, e, which_field, as_sentence=True):     
        def colorize(title_text):
            #print("colorize got:", title_text, repr(title_text), type(title_text) )
            capitalized = title_text.capitalize()
            #print("capitalized got:", capitalized, repr(capitalized), type(capitalized) )
            tag = Tag('b',capitalized)
            #print("strong got:", tag, repr(tag), type(tag) )
            #tag = Tag('span')[*capitalized]
            #tag.attributes['style'] = 'color: blue;'
            #tag = Tag('span')[Text(capitalized)]
            #tag.attributes['style'] = 'color: blue;'
            return tag
            #return capitalized    
        formatted_title = field(
            which_field, apply_func=colorize
        ) 
        if as_sentence:
            return sentence [ formatted_title ]
        else:
            return formatted_title

    def format_url(self, e):
        pdf_icon = Tag('span', '\U0001F4E5')
        space_icon = Tag('span', '\u00A0')
        return words [
            href [
                field('url', raw=True),
                Protected(pdf_icon, space_icon, 'PDF')
                ]
        ]        
            
    #def format_entry(self, label, entry, bib_data=None):
    #        context = {
    #            'entry': entry,
    #            'style': self,
    #            'bib_data': bib_data,
    #        }
    #        try:
    #            get_template = getattr(self, 'get_{}_template'.format(entry.type))
    #        except AttributeError:
    #            format_method = getattr(self, "format_" + entry.type)
    #            text = format_method(context)
    #        else:
    #            text = get_template(entry).format_data(context)
    #        spaced_text = Text(text, Protected("sdf\n\nHellooooo"))
    #        return FormattedEntry(entry.key, spaced_text, label)
            

