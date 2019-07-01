# Import
import numpy as np

#Complex Type Class
class CT_Box:
    def __init__(self, BoxString):
        BoxString = BoxString.split(' ')
        self.__x = float(BoxString[0])
        self.__y = float(BoxString[1])
        self.__width = float(BoxString[2])
        self.__height = float(BoxString[3])

class CT_CTM:
    def __init__(self, Ctm_String):
        Ctm_String = Ctm_String.split(' ')
        self.__CTM = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]], dtype = float)
        self.__CTM[0][0] = float(Ctm_String[0])
        self.__CTM[0][1] = float(Ctm_String[1])
        self.__CTM[1][0] = float(Ctm_String[2])
        self.__CTM[1][1] = float(Ctm_String[3])
        self.__CTM[2][0] = float(Ctm_String[4])
        self.__CTM[2][1] = float(Ctm_String[5])


class CT_Path:
    def __init__(self):
        self.__ID = ''
        self.__Boundary = []
        self.__AbbreviatedData = []
        #select ↓
        self.__Stroke = True #default
        self.__Fill = False
        self.__Rule = '' # NonZero or EvenOdd
        self.__FillColor = ['255', '255', '255']
        self.__StrokeColor = ['0', '0', '0']

    def get_ID(self):
        return self.__ID
    def set_ID(self, id):
        self.__ID = id

    def get_Boundary(self):
        return self.__Boundary
    def set_Boundary(self, box):
        self.__Boundary = CT_Box(box)

    def get_AbbreviatedData(self):
        return self.__AbbreviatedData
    def set_AbbreviatedData(self, data):
        self.__AbbreviatedData = data.split(' ')
    #select ↓
    def get_select_Stroke(self):
        return self.__Stroke
    def set_select_Stroke(self, Bool):
        assert Bool.lower() in ['true', 'false'], '.__Stroke is not bool.'
        self.__Stroke = Bool.lower() == 'true'

    def get_select_Fill(self):
        return self.__Fill
    def set_select_Fill(self, Bool):
        assert Bool.lower() in ['true', 'false'], '.__Fill is not bool.'
        self.__Fill = Bool.lower() == 'true'

    def get_select_Rule(self):
        return self.__Rule
    def set_select_Rule(self, Rule):
        assert Rule in ['NonZero', 'Even-Odd'], '.__Rule define the error.'
        self.__Rule = Rule

    def get_select_FillColor(self):
        return self.__FillColor
    def set_select_FillColor(self, Color):
        self.__FillColor = Color.split(' ')
        
    def get_select_StrokeColor(self):
        return self.__StrokeColor
    def set_select_StrokeColor(self, Color):
        self.__StrokeColor = Color.split(' ')


class CT_Text:
    def __init__(self):
        self.__ID = ''
        self.__Boundary = []
        self.__Size = 0.0
        self.__Font = ''
        self.__TextCode = TextCode()
        #select ↓
        self.__CGTransform = CGTransform()

    def get_ID(self):
        return self.__ID
    def set_ID(self, id):
        self.__ID = id
    
    def get_Boundary(self):
        return self.__Boundary
    def set_Boundary(self, box):
        self.__Boundary = CT_Box(box)

    def get_Size(self):
        return self.__Size
    def set_Size(self, size):
        self.__Size = float(size)

    def get_Font(self):
        return self.__Font
    def set_Font(self, font):
        self.__Font = font

    
    def get_TextCode(self):
        return self.__TextCode
    def set_TextCode(self, textcode):
        self.__TextCode = textcode


    def get_select_CGTransform(self):
        return self.__CGTransform
    def set_select_CGTransform(self, transform):
        self.__CGTransform = transform


class CT_Image:
    def __init__(self):
        self.__ID = ''
        self.__Boundary = []
        self.__CTMArray = np.empty([3,3],dtype = float)
        self.__ResourseID = ''
    
    def get_ID(self):
        return self.__ID
    def set_ID(self, id):
        self.__ID = id
    
    def get_Boundary(self):
        return self.__Boundary
    def set_Boundary(self, box):
        self.__Boundary = CT_Box(box)

    def get_CTM(self):
        return self.__CTMArray
    def set_CTM(self, Ctm_String):
        self.__CTMArray = CT_CTM(Ctm_String)

    def get_ResourseID(self):
        return self.__ResourseID
    def set_ResourceID(self, resourceid):
        self.__ResourseID = resourceid
    

class CT_Composite:
    def __init__(self):
        self.__ResourseID = ''
    
    def get_ResourseID(self):
        return self.__ResourseID
    def set_ResourceID(self, resourceid):
        self.__ResourseID = resourceid


class CT_PageBlock:
    def __init__(self):
        self.__PathObject = [] #CT_Path()
        self.__TextObject = [] #CT_Text()
        self.__ImageObject = [] #CT_Image()
        self.__CompositeObject = [] #CT_Composite()

    def get_PathObject(self):
        return self.__PathObject
    def set_PathObject(self, pathobject):
        self.__PathObject.append(pathobject)
    
    def get_TextObject(self):
        return self.__TextObject
    def set_TextObject(self, textobject):
        self.__TextObject.append(textobject)

    def get_ImageObject(self):
        return self.__ImageObject
    def set_ImageObject(self, imageobject):
        self.__ImageObject.append(imageobject)

    def get_CompositeObject(self):
        return self.__CompositeObject
    def set_CompositeObject(self, compositeobject):
        self.__CompositeObject.append(compositeobject)


class CT_VectorG:
    def __init__(self):
        self.__Width = 0.0
        self.__Height = 0.0

    def get_Width(self):
        return self.__Width
    def set_Width(self, width):
        self.__Width = width

    def get_Height(self):
        return self.__Height
    def set_Height(self, height):
        self.__Height = height


class CGTransform:
    def __init__(self):
        self.__CodePosition = 0
        #select ↓
        self.__CodeCount = 0
        self.__GlyphCount = 0
        self.__Glyphs = []

    def get_CodePosition(self):
        return self.__CodePosition
    def set_CodePosition(self, pos_string):
        self.__CodePosition = int(pos_string)

    def get_select_CodeCount(self):
        return self.__CodeCount
    def set_select_CodePosition(self, count_string):
        self.__CodeCount = int(count_string)

    def get_select_GlyphCount(self):
        return self.__GlyphCount
    def set_select_GlyphCount(self, count_string):
        self.__GlyphCount = int(count_string)

    def get_select_Glyphs(self):
        return self.__Glyphs
    def set_select_Glyphs(self, glyphs):
        self.__Glyphs = glyphs


class TextCode:
    def __init__(self):
        self.__TextValue = ''
        #select ↓
        self.__X = ''
        self.__Y = ''
        self.__DeltaX = []
        self.__DeltaY = []
    
    def get_TextValue(self):
        return self.__TextValue
    def set_TextValue(self, textvalue):
        self.__TextValue = textvalue

    def get_select_X(self):
        return self.__X
    def set_select_X(self, x):
        self.__X = float(x)

    def get_select_Y(self):
        return self.__Y
    def set_select_Y(self, y):
        self.__Y = float(y)

    def get_select_DeltaX(self):
        return self.__DeltaX
    def set_select_DeltaX(self, deltax):
        self.__DeltaX.append(int(num) for num in deltax.split(' '))

    def get_select_DeltaY(self):
        return self.__DeltaY
    def set_select_DeltaY(self, deltay):
        self.__DeltaY.append(int(num) for num in deltay.split(' '))


class CT_Font:
    def __init__(self):
        self.__FontName = ''
        self.__ID = ''
        #select ↓
        self.__FamilyName = ''
        self.__FontFile = ''
    
    def get_FontName(self):
        return self.__FontName
    def set_FontName(self, fontname):
        self.__FontName = fontname

    def get_ID(self):
        return self.__ID
    def set_ID(self, id):
        self.__ID = id

    def get_select_FamilyName(self):
        return self.__FamilyName
    def set_select_FamilyName(self, familyname):
        self.__FamilyName = familyname

    def get_select_FontFile(self):
        return self.__FontFile
    def set_select_FontFile(self, fontfile):
        self.__FontFile = fontfile


class CT_MultiMedia:
    def __init__(self):
        self.__ID = ''
        self.__Type = ''
        self.__MediaFile = ''
        #select ↓
        self.__Format = ''

    def get_ID(self):
        return self.__ID
    def set_ID(self, id):
        self.__ID = id
    
    def get_Type(self):
        return self.__Type
    def set_Type(self, types):
        self.__Type = types

    def get_MediaFile(self):
        return self.__MediaFile
    def set_MediaFile(self, mediafile):
        self.__MediaFile = mediafile

    def get_select_Format(self):
        return self.__Format
    def set_select_Format(self, format):
        self.__Format = format


#Ofd Class
class DocInfo:
    def __init__(self):
        self.__DocId = ''

    def get_DocId(self):
        return self.__DocId
    def set_DocId(self,docid):
        self.__DocId = docid


class DocBody:
    def __init__(self):
        self.__DocInfo = DocInfo()
        self.__DocRoot = ''
    
    def get_DocInfo(self):
        return self.__DocInfo
    def set_DocInfo(self, docinfo):
        self.__DocInfo = docinfo

    def get_DocRoot(self):
        return self.__DocRoot
    def set_DocRoot(self, docroot):
        self.__DocRoot = docroot
        

class OFD:
    def __init__(self):
        self.__Version = ''
        self.__DocType = ''
        self.__DocBodies = DocBody()
    
    def get_Version(self):
        return self.__Version
    def set_Version(self, version):
        self.__Version = version

    def get_DocType(self):
        return self.__DocType
    def set_DocType(self, doctype):
        self.__DocType = doctype

    def get_DocBodies(self):
        return self.__DocBodies
    def set_DocBodies(self, docbodies):
        self.__DocBodies = docbodies

#Document Class
class CommonData:
    def __init__(self):
        self.__MaxUnitId = ''
        self.__PageArea = ''
        self.__PublicRes = ''
        self.__DocumentRes = ''
    
    def get_MaxUnitId(self):
        return self.__MaxUnitId
    def set_MaxUnitId(self, maxunitid):
        self.__MaxUnitId = maxunitid

    def get_PageArea(self):
        return self.__PageArea
    def set_PageArea(self, pagearea):
        self.__PageArea = pagearea

    def get_PublicRes(self):
        return self.__PublicRes
    def set_PublicRes(self, publicres):
        self.__PublicRes = publicres

    def get_DocumentRes(self):
        return self.__DocumentRes
    def set_DocumentRes(self, documentres):
        self.__DocumentRes = documentres


class PageArea:
    def __init__(self):
        self.__PhysicalBox = []
        #select ↓
        self.__ApplicationBox = []
        self.__ContentBox = []  
        self.__BleedBox = []

    def get_PhysicalBox(self):
        return self.__PhysicalBox
    def set_PhysicalBox(self, box):
        self.__PhysicalBox = CT_Box(box)

    def get_select_ApplicationBox(self):
        return self.__ApplicationBox
    def set_select_ApplicationBox(self, box):
        self.__ApplicationBox = CT_Box(box)

    def get_select_ContentBox(self):
        return self.__ContentBox
    def set_select_ContentBox(self, box):
        self.__ContentBox = CT_Box(box)

    def get_select_BleedBox(self):
        return self.__BleedBox
    def set_select_BleedBox(self, box):
        self.__BleedBox = CT_Box(box)


class PageNode:
    def __init__(self):
        self.BaseLoc = ''
        self.ID = ''
    

class Document:
    def __init__(self):
        self.__CommonData = CommonData()
        self.__Pages = []
        #select ↓
        self.__Annotations = '' 

    def get_CommonData(self):
        return self.__CommonData
    def set_CommonData(self, commondata):
        self.__CommonData = commondata

    def get_Pages(self):
        return self.__Pages
    def set_Pages(self, pages):
        self.__Pages.append(pages)

    def get_select_Annotations(self):
        return self.__Annotations
    def set_select_Annotations(self, annotations):
        self.__Annotations = annotations

#Page Class
class Layer:
    def __init__(self):
        self.__LayerId = ''
        self.__PageBlock = CT_PageBlock()
        
    def get_LayerId(self):
        return self.__LayerId
    def set_LayerId(self, layerid):
        self.__LayerId = layerid

    def get_PageBlock(self):
        return self.__PageBlock
    def set_PageBlock(self, pageblock):
        self.__PageBlock = pageblock


class Content:
    def __init__(self):
        self.__Layer = Layer()
    
    def get_Layer(self):
        return self.__Layer
    def set_Layer(self, layer):
        self.__Layer = layer
       

class Page:
    def __init__(self):
        #select ↓
        self.__Area = PageArea()
        self.__Template = '' #Template()
        self.__PageRes = '' #PageRes()
        self.__Content = Content()
        self.__Actions = '' #Actions()

    def get_select_Area(self):
        return self.__Area
    def set_select_Area(self, area):
        self.__Area = area

    def get_select_Content(self):
        return self.__Content
    def set_select_Content(self, content):
        self.__Content = content


class Pages:
    def __init__(self):
        self.__PageID = ''
        self.__PageN = Page()
    
    def get_PageID(self):
        return self.__PageID
    def set_PageID(self, pageid):
        self.__PageID = pageid

    def get_PageN(self):
        return self.__PageN
    def set_PageN(self, page):
        self.__PageN = page


#PublicRes Class
class PublicRes:
    def __init__(self):
        self.BaseLoc = ''
        self.__Fonts = []

    def get_Fonts(self):
        return self.__Fonts
    def set_Fonts(self, font):
        self.__Fonts.append(font)


#DocumentRes Class
class DocumentRes:
    def __init__(self):
        self.BaseLoc = ''
        self.__MultiMedias = []

    def get_MultiMedias(self):
        return self.__MultiMedias
    def set_MultiMedias(self, meida):
        self.__MultiMedias.append(meida)

    

    
