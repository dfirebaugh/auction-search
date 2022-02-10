from datetime import datetime
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus.tables import Flowable
from reportlab.platypus.flowables import Image, HRFlowable
from reportlab.lib.styles import StyleSheet1, ParagraphStyle
from reportlab.lib.units import cm

class StyleSheet(StyleSheet1, Flowable):
    "provides required overrides for StyleSheet1 and Flowable"
    def __init__(self):
        self.width = 0
        self.height = 0
        self.wrapped = 0

        #these are hints to packers/frames as to how the floable should be positioned
        self.hAlign = 'LEFT'    #CENTER/CENTRE or RIGHT
        self.vAlign = 'BOTTOM'  #MIDDLE or TOP

        #optional holder for trace info
        self._traceInfo = None
        self._showBoundary = None

        #many flowables handle text and must be processed in the
        #absence of a canvas.  tagging them with their encoding
        #helps us to get conversions right.  Use Python codec names.
        self.encoding = None
    def draw(self):
        return False
    def getKeepWithNext(self):
        return False
    def getSpaceBefore(self):
        return 0

def generate_pdf(search_term="", upper_price_limit="", auctions=[]):
    now = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    filename = 'output.'+search_term+'.'+upper_price_limit+'.'+now+'.pdf'
    print("generating pdf: ", filename)
    print("wait...")

    doc = SimpleDocTemplate(filename, pagesize=A4,
        rightMargin=2*cm,leftMargin=2*cm,
        topMargin=2*cm,bottomMargin=2*cm)

    styles = StyleSheet()
    link_style = ParagraphStyle(name="link-style", textColor="blue", fontSize=20, linkUnderline=True)

    elements = []
    for auction in auctions:
        text = auction.html_text()
        paragraph = Paragraph(text)
        elements.append(Paragraph(auction.link_html_text(), style=link_style))
        elements.append(paragraph)
        for image in auction.images:
            elements.append(Image(image["src"]))
        elements.append(HRFlowable(
            color="black",
            thickness=2,
            width="100%",
        ))
    elements.append(styles)
    doc.build(elements)
