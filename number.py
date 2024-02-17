import pyqrcode

def qr_code():
    s='''Hello Friend 
    This is Ranadeb Saha
    Address:- Khajurdihi, Katwa, Purba Bardhaman, WB-713150
    Contact:- +91 6295111477
    E-mail:- ranadebsaha@yahoo.com
    Note: If any Problem in Coding(C,Java,Python,PHP,HTML,CSS,JavaScript,SQL), MS Word, Excel, PowerPoint, Tally(GST), PhotoShop then contact me fell free
    Thank You to Scan this QR Code.
    '''
    d=pyqrcode.create(s)
    d.png('my_img1.png', scale=6)
    print('code Executed')
    
qr_code()