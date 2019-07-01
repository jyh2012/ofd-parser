import zipfile
import os
from tempfile import NamedTemporaryFile

from ofd_class import CT_Box, CT_CTM, CT_Path, CT_Text, CT_Image, CT_Composite, CT_PageBlock, CT_VectorG, CGTransform, TextCode, CT_Font, CT_MultiMedia
from ofd_class import OFD, DocBody, DocInfo
from ofd_class import Document, CommonData, PageNode, PageArea
from ofd_class import Pages, Page, Content, Layer
from ofd_class import PublicRes, DocumentRes

# import lxml or ElementTree for XML parsing:
try:
    # lxml: best performance for XML processing
    import lxml.etree as ET
except ImportError:
    import xml.etree.cElementTree as ET

# docNS that have to be part of every ofd file
FILE_DOC_NS = {'ofd': 'http://www.ofdspec.org/2016'}
    

class OfdParser:
    def __init__(self,filePath):
        self.ofd_file_path = filePath
        self.ofd_temp_path = self.createTempFile()
        self.outlines_list = []
        self.OFD = self.Make_OFD(self.ofd_temp_path)
        self.Document = self.Parse_Document(self.OFD, self.ofd_temp_path)
        self.Pages = self.Parse_Pages(self.OFD, self.Document, self.ofd_temp_path)
        self.PublicRes = self.Parse_PublicRes(self.OFD, self.Document, self.ofd_temp_path)
        self.DocumentRea = self.Parse_DocumentRes(self.OFD, self.Document, self.ofd_temp_path)
    

    def unZip(self, dir, ofd_name ,temp_path):
        file_name = os.path.splitext(ofd_name)[0]
        zip_file = zipfile.ZipFile(temp_path)
        file_dir = dir + '/' + file_name + '_unzip_files'
        if not os.path.isdir(file_dir):
            os.mkdir(file_dir)
        for names in zip_file.namelist():
            zip_file.extract(names, file_dir)
        zip_file.close()
        return file_dir


    def createTempFile(self):
        # 读取OFD文件
        ofd_file = open(self.ofd_file_path, 'rb')
        ofd_dir,ofd_name = os.path.split(self.ofd_file_path)
        # 创建临时zip文件
        temp = NamedTemporaryFile(suffix='.zip', dir=ofd_dir, delete=False)
        # 获取临时文件完整路径
        temp_path = temp.name
        # print(temp_path)
        # 将OFD文件数据复制到临时zip文件中
        temp.write(ofd_file.read())
        # 解压缩
        file_dir = self.unZip(ofd_dir, ofd_name, temp_path)
        # 删除临时文件
        temp.close()
        os.remove(temp_path)
        # 返回解压缩文件夹路径
        # self.parseOFDFiles(file_dir)
        return file_dir


    def Make_OFD(self, ofd_temp_path):
        '''
        解析OFD.xml文件得到最基本的框架信息
        @param ofd_temp_path: 解压得到的文件目录
        @return ofd: 解析OFD.xml得到的文件头
        '''
        #define
        docbody = DocBody()
        docinfo = DocInfo()
        ofd = OFD()
        #parse OFD
        tree = ET.parse(ofd_temp_path + '/OFD.xml')
        root = tree.getroot()
        assert root.nsmap == FILE_DOC_NS, 'docNS is wrong'
        for i in range(len(root)):
            if 'DocBody' in root[i].tag:
                Doc_Body = root[i]
        for i in range(len(Doc_Body)):
            if 'DocRoot' in Doc_Body[i].tag:
                Doc_Root = Doc_Body[i]
            if 'DocInfo' in Doc_Body[i].tag:
                Doc_Info = Doc_Body[i]
        #set
        for i in range(len(root.items())):
            if 'Version' in root.items()[i]:
                ofd.set_Version(root.items()[i][1])
                #assert
                assert ofd.get_Version() == root.items()[i][1], 'Version is wrong'
            if 'DocType' in root.items()[i]:
                ofd.set_DocType(root.items()[i][1])
                #assert
                assert ofd.get_DocType() == root.items()[i][1], 'DocType is wrong'
        
        docinfo.set_DocId(Doc_Info.getchildren().pop().text)
        docbody.set_DocInfo(docinfo)
        docbody.set_DocRoot(Doc_Root.text)
        ofd.set_DocBodies(docbody)
        #assert
        assert ofd.get_DocBodies().get_DocInfo().get_DocId() == Doc_Info.getchildren().pop().text, 'DocId is wrong'
        assert ofd.get_DocBodies().get_DocRoot() == Doc_Root.text, 'DocType is wrong'
        #return
        return ofd


    # 解析Document.xml
    def Parse_Document(self, OFD, ofd_temp_path):
        '''
        对Document.xml文件进行解析
        @param OFD: OFD.xml解析之后的文件头
        @param ofd_temp_path: 解压之后的地址
        @return document: 解析Document.xml得到的文件头
        '''
        #define
        document = Document()
        commondata = CommonData()
        #parse Document
        file_dir = ofd_temp_path + '/' + OFD.get_DocBodies().get_DocRoot()
        tree = ET.parse(file_dir)
        root = tree.getroot()
        assert root.nsmap == FILE_DOC_NS, 'docNS is wrong'

        for i in range(len(root)):
            if 'CommonData' in root[i].tag:
                Common_Data = root[i]
            if 'Pages' in root[i].tag:
                Pages = root[i]
            if 'Annotations' in root[i].tag:
                Annotations = root[i]

        for i in range(len(Common_Data)):
            if 'MaxUnitID' in Common_Data[i].tag:
                Max_Unit_ID = Common_Data[i]
                commondata.set_MaxUnitId(Max_Unit_ID.text)
                #assert
                assert commondata.get_MaxUnitId() == Max_Unit_ID.text, 'MaxUnitID is wrong'

            if 'PageArea' in Common_Data[i].tag:
                Page_Area = Common_Data[i]
                commondata.set_PageArea(Page_Area.text)
                #assert
                assert commondata.get_PageArea() == Page_Area.text, 'PageArea is wrong'

            if 'PublicRes' in Common_Data[i].tag:
                Public_Res = Common_Data[i]
                commondata.set_PublicRes(Public_Res.text)
                #assert
                assert commondata.get_PublicRes() == Public_Res.text, 'PublicRes is wrong'

            if 'DocumentRes' in Common_Data[i].tag:
                Document_Res = Common_Data[i]
                commondata.set_DocumentRes(Document_Res.text)
                #assert
                assert commondata.get_DocumentRes() == Document_Res.text, 'DocumentRes is wrong'
        document.set_CommonData(commondata)
        for i in range(len(Pages)):
            page_N = PageNode()
            for j in range(len(Pages[i].items())):
                if 'ID' in Pages[i].items()[j]:
                    page_N.ID = Pages[i].items()[j][1]
                    #assert
                    assert page_N.ID == Pages[i].items()[j][1], 'ID is wrong'

                if 'BaseLoc' in Pages[i].items()[j]:
                    page_N.BaseLoc = Pages[i].items()[j][1]
                    #assert
                    assert page_N.BaseLoc == Pages[i].items()[j][1], 'BaseLoc is wrong'

            document.set_Pages(page_N)
        if 'Annotations' in vars():
            document.set_select_Annotations(Annotations.text)
            #assert
            assert document.get_select_Annotations() == Annotations.text, 'Annotations is wrong'

        #return
        return document


    def Parse_Pages(self, OFD, Document, ofd_temp_path):
        Page_All = []
        path = OFD.get_DocBodies().get_DocRoot().split('/')
        file_dir = ''
        for i in range(len(path)-1):
            file_dir += path[i] + '/'
        file_dir = ofd_temp_path + '/' + file_dir
        for page_i in Document.get_Pages():
            #得到每一页Page的路径和ID
            file_dir_BaseLoc = file_dir + page_i.BaseLoc
            file_dir_ID = page_i.ID
            #定义一个Pages类的page来存储当前页面的全部信息
            pages = Pages()
            page = Page()
            area = PageArea()
            pageblock = CT_PageBlock()
            content = Content()
            layer = Layer()
            pages.set_PageID(file_dir_ID)
            #开始解析
            tree = ET.parse(file_dir_BaseLoc)
            root = tree.getroot()
            assert root.nsmap == FILE_DOC_NS, 'docNS is wrong'
            for i in range(len(root)):
                if 'Area' in root[i].tag:
                    Area = root[i]
                if 'Content' in root[i].tag:
                    Contents = root[i]
            
            for item in Area:
                if 'PhysicalBox' in item.tag:
                    area.set_PhysicalBox(item.text)
                if 'ApplicationBox' in item.tag:
                    area.set_select_ApplicationBox(item.text)
                if 'ContentBox' in item.tag:
                    area.set_select_ContentBox(item.text)
                if 'BleedBox' in item.tag:
                    area.set_select_BleedBox(item.text)
            page.set_select_Area(area)

            for item in Contents:
                if 'Layer' in item.tag:
                    Layers = item
            for i in range(len(Layers.items())):
                if 'ID' in Layers.items()[i]:
                    layer.set_LayerId(Layers.items()[i][1])
            
            for obj in Layers:
                if 'PathObject' in obj.tag:
                    Path_temp = CT_Path()
                    for header in obj.items():
                        if 'ID' in header:
                            Path_temp.set_ID(header[1])
                        if 'Boundary' in header:
                            Path_temp.set_Boundary(header[1])
                        if 'Stroke' in header:
                            Path_temp.set_select_Stroke(header[1])
                        if 'Fill' in header:
                            Path_temp.set_select_Fill(header[1])
                        if 'Rule' in header:
                            Path_temp.set_select_Rule(header[1])
                    for item in obj:
                        if 'AbbreviatedData' in item.tag:
                            Path_temp.set_AbbreviatedData(item.text)
                        if 'FillColor' in item.tag:
                            for i in range(len(item.items())):
                                if 'Value'in item.items():
                                    Path_temp.set_select_FillColor(item.items()[0][1])
                        if 'StrokeColor' in item.tag:
                            for i in range(len(item.items())):
                                if 'Value'in item.items():
                                    Path_temp.set_select_StrokeColor(item.items()[0][1])
                    pageblock.set_PathObject(Path_temp)
                
                if 'TextObject' in obj.tag:
                    Text_temp = CT_Text()
                    for header in obj.items():
                        if 'ID' in header:
                            Text_temp.set_ID(header[1])
                        if 'Boundary' in header:
                            Text_temp.set_Boundary(header[1])
                        if 'Size' in header:
                            Text_temp.set_Size(header[1])
                        if 'Font' in header:
                            Text_temp.set_Font(header[1])
                    for item in obj:
                        if 'CGTransform' in item.tag:
                            CGTransform_temp = CGTransform()
                            for second_header in item.items():
                                if 'CodePosition' in second_header:
                                    CGTransform_temp.set_CodePosition(second_header[1])
                                if 'CodeCount' in second_header:
                                    CGTransform_temp.set_select_CodePosition(second_header[1])
                                if 'GlyphCount' in second_header:
                                    CGTransform_temp.set_select_GlyphCount(second_header[1])
                            for second_item in item:
                                if 'Glyphs' in second_item.tag:
                                    CGTransform_temp.set_select_Glyphs(second_item.text)
                            Text_temp.set_select_CGTransform(CGTransform_temp)
                        if 'TextCode' in item.tag:
                            TextCode_temp = TextCode()
                            TextCode_temp.set_TextValue(item.text)
                            for second_header in item.items():
                                if 'X' in second_header:
                                    TextCode_temp.set_select_X(second_header[1])
                                if 'Y' in second_header:
                                    TextCode_temp.set_select_Y(second_header[1])
                                if 'DeltaX' in second_header:
                                    TextCode_temp.set_select_DeltaX(second_header[1])
                                if 'DeltaY' in second_header:
                                    TextCode_temp.set_select_DeltaY(second_header[1])
                            Text_temp.set_TextCode(TextCode_temp)
                        pageblock.set_TextObject(Text_temp)

                if 'ImageObject' in obj.tag:
                    Image_temp = CT_Image()
                    for header in obj.items():
                        if 'ID' in header:
                            Image_temp.set_ID(header[1])
                        if 'Boundary' in header:
                            Image_temp.set_Boundary(header[1])
                        if 'CTM' in header:
                            Image_temp.set_CTM(header[1])
                        if 'ResourceID' in header:
                            Image_temp.set_ResourceID(header[1])
                    pageblock.set_ImageObject(Image_temp)

                if 'CompositeObject' in obj.tag:
                    Composite_temp = CT_Composite()
                    for header in obj.items():
                        if 'ResourceID' in header:
                            Composite_temp.set_ResourceID(header[1])
                    pageblock.set_CompositeObject(Composite_temp)
            layer.set_PageBlock(pageblock)             
            content.set_Layer(layer)
            page.set_select_Content(content)
            pages.set_PageN(page)
            Page_All.append(pages)
        return Page_All


    def Parse_PublicRes(self, OFD, Document, ofd_temp_path):
        path = OFD.get_DocBodies().get_DocRoot().split('/')
        file_dir = ''
        for i in range(len(path)-1):
            file_dir += path[i] + '/'
        file_dir = ofd_temp_path + '/' + file_dir + Document.get_CommonData().get_PublicRes()
        #定义
        publicres = PublicRes()
        #开始解析
        tree = ET.parse(file_dir)
        root = tree.getroot()
        assert root.nsmap == FILE_DOC_NS, 'docNS is wrong'
        for header in root.items():
            if 'BaseLoc' in header:
                publicres.BaseLoc = header[1]
        
        for i in range(len(root)):
            if 'Fonts' in root[i].tag:
                Fonts = root[i]

        for item in Fonts:
            font = CT_Font()
            for header in item.items():
                if 'ID' in header:
                    font.set_ID(header[1])
                if 'FontName' in header:
                    font.set_FontName(header[1])
                if 'FamiltName' in header:
                    font.set_select_FamilyName(header[1])
            for second_item in item:
                if 'FontFile' in second_item.tag:
                    font.set_select_FontFile(second_item.text)
            publicres.set_Fonts(font)
        
        return publicres

    
    def Parse_DocumentRes(self, OFD, Document, ofd_temp_path):
        path = OFD.get_DocBodies().get_DocRoot().split('/')
        file_dir = ''
        for i in range(len(path)-1):
            file_dir += path[i] + '/'
        file_dir = ofd_temp_path + '/' + file_dir + Document.get_CommonData().get_DocumentRes()
        #定义
        documentres = DocumentRes()
        #开始解析
        tree = ET.parse(file_dir)
        root = tree.getroot()
        assert root.nsmap == FILE_DOC_NS, 'docNS is wrong'
        for header in root.items():
            if 'BaseLoc' in header:
                documentres.BaseLoc = header[1]
        
        for i in range(len(root)):
            if 'MultiMedias' in root[i].tag:
                MultiMedias = root[i]

        for item in MultiMedias:
            media = CT_MultiMedia()
            for header in item.items():
                if 'ID' in header:
                    media.set_ID(header[1])
                if 'Type' in header:
                    media.set_Type(header[1])
                if 'Format' in header:
                    media.set_select_Format(header[1])
            for second_item in item:
                if 'MediaFile' in second_item.tag:
                    media.set_MediaFile(second_item.text)
            documentres.set_MultiMedias(media)

        return documentres


def main():
    file_dir = 'C:\\Users\\jiayi\\Desktop\\ooxml\\文件识别.ofd'
    Ofd_Parser = OfdParser(file_dir)
    print('a')
    
        



if __name__ == '__main__':
    main()

