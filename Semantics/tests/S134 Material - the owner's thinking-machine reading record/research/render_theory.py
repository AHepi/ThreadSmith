from pathlib import Path
from xml.sax.saxutils import escape
import json
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

ROOT=Path(__file__).parent
OUT=ROOT.parents[1]/'output'
OUT.mkdir(exist_ok=True)
pdfmetrics.registerFont(TTFont('ReaderSerif','/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('ReaderSerifBold','/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('ReaderSans','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
styles={
 'title':ParagraphStyle('title',fontName='ReaderSerifBold',fontSize=24,leading=30,textColor=HexColor('#183c48'),spaceAfter=16),
 'subtitle':ParagraphStyle('subtitle',fontName='ReaderSans',fontSize=10,leading=15,textColor=HexColor('#536971'),spaceAfter=18),
 'heading':ParagraphStyle('heading',fontName='ReaderSerifBold',fontSize=13,leading=18,textColor=HexColor('#183c48'),spaceBefore=13,spaceAfter=9,keepWithNext=True),
 'body':ParagraphStyle('body',fontName='ReaderSerif',fontSize=10.2,leading=14.3,spaceAfter=9,alignment=TA_LEFT,allowWidows=0,allowOrphans=0),
 'small':ParagraphStyle('small',fontName='ReaderSans',fontSize=8.8,leading=12.5,spaceAfter=9),
}

def footer(canv,doc):
    canv.saveState()
    canv.setStrokeColor(HexColor('#ccd8da'));canv.setLineWidth(.5)
    canv.line(48,42,A4[0]-48,42)
    canv.setFillColor(HexColor('#536971'));canv.setFont('ReaderSans',8)
    canv.drawString(48,29,'A theory for creating a thinking machine')
    canv.drawRightString(A4[0]-48,29,f'Page {doc.page}')
    canv.restoreState()

def main():
    report=json.loads((ROOT/'theory_content.json').read_text())
    story=[Paragraph(escape(report['title']),styles['title']),Paragraph(escape(report['subtitle']),styles['subtitle'])]
    text=[report['title'],report['subtitle'],'']
    for section in report['sections']:
        if section.get('title'):
            story.append(Paragraph(escape(section['title']),styles['heading']))
            text.extend([section['title'],''])
        for para in section['paragraphs']:
            story.append(Paragraph(escape(para).replace('\n','<br/>'),styles['small' if section.get('small') else 'body']))
            text.extend([para,''])
    target=OUT/'Thinking_Machine_Theory.pdf'
    doc=SimpleDocTemplate(str(target),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=46,bottomMargin=56,title=report['title'],author='OpenAI Codex, with source readings by MiMo 2.6 Pro')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    (OUT/'Thinking_Machine_Theory.txt').write_text('\n'.join(text))
    print(str(target))

if __name__=='__main__':main()
