from PIL import Image, ImageDraw, ImageFont
import math
ROOT='/data/data/com.termux/files/home/tahdiri-summary-ad'; F=ROOT+'/assets/fonts/Cairo-Variable.ttf'; W,H=1080,1920
teal='#55d4c4'; gold='#f2c66d'; ivory='#f4f7f6'; muted='#aab9b7'; dark='#101719'
def font(sz,weight=500): return ImageFont.truetype(F,sz,layout_engine=ImageFont.Layout.RAQM)
def rr(d,b,r,fill,outline=None,width=1): d.rounded_rectangle(b,radius=r,fill=fill,outline=outline,width=width)
def base(kicker):
 im=Image.new('RGB',(W,H),dark); d=ImageDraw.Draw(im)
 for y in range(H):
  glow=max(0,1-abs(y-220)/1100); d.line((0,y,W,y),fill=(16,int(23+35*glow),int(25+35*glow)))
 d.ellipse((760,-190,1310,360),fill='#163b39'); d.ellipse((-360,1390,260,2010),fill='#142c2b')
 d.text((W-74,82),'TAHDIRI  /  تحضيري',font=font(30,700),fill=ivory,anchor='ra',direction='rtl',language='ar'); d.rounded_rectangle((74,152,260,160),4,fill=teal)
 if kicker: d.text((W-74,205),kicker,font=font(27,600),fill=teal,anchor='ra',direction='rtl',language='ar')
 return im
def summary(path,second=False):
 im=base('ملخصات مرتبة • مثال تجريبي عام'); d=ImageDraw.Draw(im); rr(d,(105,325,975,1570),76,'#202d30','#57716e',4); rr(d,(133,358,947,1534),52,'#f6f7f3'); rr(d,(452,378,628,394),8,'#9eaaa6')
 d.text((900,470),'ملخصاتي',font=font(43,700),fill='#172322',anchor='ra',direction='rtl',language='ar'); d.text((900,527),'محتوى توضيحي غير منهجي',font=font(24),fill='#71807c',anchor='ra',direction='rtl',language='ar')
 rr(d,(187,570,893,660),25,'#e8f5f2'); d.text((850,615),'مثال تجريبي عام',font=font(28,600),fill='#087e73',anchor='ra',direction='rtl',language='ar')
 if not second:
  rr(d,(187,700,893,1055),32,'#ffffff','#e2e9e5',2); d.text((842,760),'عنوان توضيحي',font=font(35,700),fill='#1b2927',anchor='ra',direction='rtl',language='ar'); d.text((842,817),'فكرة رئيسية',font=font(26,600),fill='#087e73',anchor='ra',direction='rtl',language='ar')
  for i,t in enumerate(['معلومة مختصرة وواضحة','نقطة أساسية سهلة التذكر','ترتيب يساعد على الفهم']):
   y=885+i*52; d.ellipse((235,y+9,253,y+27),fill=gold); d.text((842,y),t,font=font(23),fill='#384643',anchor='ra',direction='rtl',language='ar')
  rr(d,(187,1090,893,1280),28,'#fff8e9'); d.text((842,1140),'تذكّر الفكرة',font=font(26,700),fill='#83601b',anchor='ra',direction='rtl',language='ar'); d.text((842,1190),'مثال تجريبي عام',font=font(23),fill='#65583c',anchor='ra',direction='rtl',language='ar')
 else:
  for i,(title,sub) in enumerate([('مفهوم تجريبي','نقاط مختصرة للمراجعة'),('فكرة رئيسية','معلومة واضحة ومنظمة'),('مراجعة سريعة','مثال توضيحي عام')]):
   y=700+i*185; rr(d,(187,y,893,y+150),28,'#ffffff','#e2e9e5',2); rr(d,(215,y+25,275,y+85),18,'#e5f5f1'); d.text((245,y+55),str(i+1),font=font(28,700),fill='#087e73',anchor='mm'); d.text((842,y+45),title,font=font(29,700),fill='#1b2927',anchor='ra',direction='rtl',language='ar'); d.text((842,y+98),sub,font=font(22),fill='#71807c',anchor='ra',direction='rtl',language='ar')
 rr(d,(187,1360,893,1465),26,'#087e73'); d.text((540,1413),'محتوى تجريبي للعرض فقط',font=font(25,600),fill='white',anchor='mm',direction='rtl',language='ar'); im.save(path)
def end(path):
 im=base(''); d=ImageDraw.Draw(im); rr(d,(355,390,725,760),82,'#0f5f5c'); d.line((462,520,618,520),fill='#ffffff',width=30); d.line((540,520,540,652),fill='#ffffff',width=30); d.line((484,652,596,652),fill='#ffffff',width=30); d.ellipse((595,588,635,628),fill='#e0a526')
 d.text((540,930),'تحضيري',font=font(88,700),fill=ivory,anchor='mm',direction='rtl',language='ar'); d.text((540,1070),'تحضيري... خلّي دراستك أسهل',font=font(53,600),fill=teal,anchor='mm',direction='rtl',language='ar'); rr(d,(328,1190,752,1200),5,gold); d.text((540,1310),'ملخصات تساعدك على تنظيم المراجعة',font=font(27),fill=muted,anchor='mm',direction='rtl',language='ar'); d.text((540,1690),'TAHDIRI',font=font(30,700),fill='#6c8380',anchor='mm'); im.save(path)
summary(ROOT+'/scenes/summary-one.png'); summary(ROOT+'/scenes/summary-two.png',True); end(ROOT+'/scenes/endcard.png')
