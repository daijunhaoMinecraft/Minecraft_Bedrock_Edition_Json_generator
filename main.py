# -*- coding:utf-8 -*-
import json
import ast
import wx
import re
from Taowa_wx import *
from Taowa_skin import *
from ObjectListView import ObjectListView, ColumnDefn
import pyperclip3 as pycopy


皮肤_加载(皮肤.Areo)

text_json = {
    "rawtext":[]
}

class MyObject:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Frame(wx_Frame):
    def __init__(self):
        wx_Frame.__init__(self, None, title='tellraw/titleraw可视化编辑器', size=(1524, 867),name='frame',style=541072384)
        self.启动窗口 = wx_StaticText(self)
        self.Centre()
        self.超级列表框1 = ObjectListView(self.启动窗口,size=(906, 302),pos=(29, 43),name='listCtrl',style=8227)
        self.超级列表框1.SetColumns([
            ColumnDefn("序号", "left", 112, "one"),
            ColumnDefn("事件", "left", 787, "two")
        ])
        self.标签1 = wx_StaticTextL(self.启动窗口,size=(674, 24),pos=(29, 14),label='当前json大致内容:',name='staticText',style=1)
        self.标签2 = wx_StaticTextL(self.启动窗口,size=(80, 24),pos=(29, 500),label='纯文本类型:',name='staticText',style=1)
        self.标签3 = wx_StaticTextL(self.启动窗口,size=(60, 24),pos=(29, 520),label='文本内容:',name='staticText',style=0)
        self.text_text = wx_TextCtrl(self.启动窗口,size=(840, 22),pos=(95, 522),value='',name='text',style=0 | wx.TE_MULTILINE)
        self.标签4 = wx_StaticTextL(self.启动窗口,size=(242, 24),pos=(29, 581),label='实体选择器:',name='staticText',style=1)
        self.标签5 = wx_StaticTextL(self.启动窗口,size=(93, 24),pos=(29, 602),label='实体选择与参数:',name='staticText',style=1)
        self.selector_text = wx_TextCtrl(self.启动窗口,size=(811, 22),pos=(124, 604),value='',name='text',style=0 | wx.TE_MULTILINE)
        self.标签6 = wx_StaticTextL(self.启动窗口,size=(80, 24),pos=(29, 663),label='计分版类型:',name='staticText',style=1)
        self.add_text = wx_Button(self.启动窗口,size=(80, 32),pos=(29, 545),label='添加文本',name='button')
        self.add_text.Bind(wx.EVT_BUTTON,self.add_text_按钮被单击)
        self.add_selector = wx_Button(self.启动窗口,size=(80, 32),pos=(29, 626),label='添加选择器',name='button')
        self.add_selector.Bind(wx.EVT_BUTTON,self.add_selector_按钮被单击)
        self.标签7 = wx_StaticTextL(self.启动窗口,size=(80, 24),pos=(29, 688),label='计分板实体:',name='staticText',style=1)
        self.score_selector = wx_TextCtrl(self.启动窗口,size=(823, 22),pos=(112, 690),value='',name='text',style=0 | wx.TE_MULTILINE)
        self.标签8 = wx_StaticTextL(self.启动窗口,size=(80, 24),pos=(29, 715),label='计分板名称:',name='staticText',style=1)
        self.score_name = wx_TextCtrl(self.启动窗口,size=(823, 22),pos=(112, 717),value='',name='text',style=0 | wx.TE_MULTILINE)
        self.add_score = wx_Button(self.启动窗口,size=(80, 32),pos=(29, 744),label='添加计分板',name='button')
        self.add_score.Bind(wx.EVT_BUTTON,self.add_score_按钮被单击)
        self.generate_json = wx_Button(self.启动窗口,size=(80, 32),pos=(29, 356),label='生成json',name='button')
        self.generate_json.Bind(wx.EVT_BUTTON,self.generate_json_按钮被单击)
        self.编辑框5 = wx_TextCtrl(self.启动窗口,size=(726, 22),pos=(124, 363),value='',name='text',style=16)
        self.copy_json = wx_Button(self.启动窗口,size=(80, 32),pos=(855, 360),label='复制内容',name='button')
        self.copy_json.Bind(wx.EVT_BUTTON,self.copy_json_按钮被单击)
        self.delete_content = wx_Button(self.启动窗口,size=(101, 32),pos=(29, 402),label='删除此序号内容',name='button')
        self.delete_content.Bind(wx.EVT_BUTTON,self.delete_content_按钮被单击)
        self.revise_json = wx_Button(self.启动窗口,size=(101, 32),pos=(29, 442),label='修改此序号内容',name='button')
        self.revise_json.Bind(wx.EVT_BUTTON,self.revise_json_按钮被单击)
        self.read_json = wx_Button(self.启动窗口,size=(80, 32),pos=(156, 402),label='读取json内容',name='button')
        self.read_json.Bind(wx.EVT_BUTTON,self.read_json_按钮被单击)
        self.编辑框6 = wx_TextCtrl(self.启动窗口,size=(679, 22),pos=(250, 409),value='',name='text',style=0)
        self.flushed_content = wx_Button(self.启动窗口,size=(80, 32),pos=(855, 7),label='刷新内容',name='button')
        self.flushed_content.Bind(wx.EVT_BUTTON,self.flushed_content_按钮被单击)
        self.标签9 = wx_StaticTextL(self.启动窗口,size=(80, 24),pos=(967, 181),label='变量类型:',name='staticText',style=1)
        self.标签10 = wx_StaticTextL(self.启动窗口,size=(56, 24),pos=(967, 202),label='文本内容:',name='staticText',style=1 | wx.TE_MULTILINE)
        self.编辑框7 = wx_TextCtrl(self.启动窗口,size=(494, 171),pos=(967, 7),value='如果你不引用变量的话,那么建议还是使用"纯文本类型"添加文本\n变量引用方法:比如说我变量内容为"world;hello"，而我想输出"hello world"那么文本内容需要输入"%%2 world"首先"%%2"为引用变量,末尾的数字代表着从左到右开始数(这里显示的分号俩边分别为1和2)\n再次演示:比如我的变量内容为"hello;world;map",而我想在变量里面只输出map,那么变量内容输入"hello;world;map",文本内容输入%%3,这样就完成输出"map"\n可参考wiki: https://minecraft.fandom.com/zh/wiki/%E5%9F%BA%E5%B2%A9%E7%89%88%E5%8E%9F%E5%A7%8BJSON%E6%96%87%E6%9C%AC%E6%A0%BC%E5%BC%8F',name='text',style=1073745968)
        self.text_text_1 = wx_TextCtrl(self.启动窗口,size=(426, 22),pos=(1035, 204),value='',name='text',style=0)
        self.标签11 = wx_StaticTextL(self.启动窗口,size=(57, 24),pos=(967, 229),label='变量内容:',name='staticText',style=1 | wx.TE_MULTILINE)
        self.path_content = wx_TextCtrl(self.启动窗口,size=(426, 22),pos=(1035, 231),value='',name='text',style=0)
        self.add_path_text = wx_Button(self.启动窗口,size=(80, 32),pos=(967, 260),label='添加文本',name='button')
        self.add_path_text.Bind(wx.EVT_BUTTON,self.add_path_text_按钮被单击)
        self.编辑框10 = wx_TextCtrl(self.启动窗口,size=(494, 422),pos=(967, 324),value='',name='text',style=1073745952 | wx.TE_READONLY)
        self.标签12 = wx_StaticTextL(self.启动窗口,size=(80, 24),pos=(967, 295),label='输出内容:',name='staticText',style=1)
        self.generate_json.Disable()

        self.超级列表框1.Bind(wx.EVT_RIGHT_DOWN, self.on_right_click)

        self.popup_menu = wx.Menu()
        delete_item = self.popup_menu.Append(-1, '删除')
        fix_item = self.popup_menu.Append(-1, '修改')
        self.popup_menu.AppendSeparator()
        clean_item = self.popup_menu.Append(-1, '清空列表')
        self.Bind(wx.EVT_MENU, self.delete_content_按钮被单击, delete_item)
        self.Bind(wx.EVT_MENU, self.revise_json_按钮被单击, fix_item)
        self.Bind(wx.EVT_MENU, self.clean_item_everyone, clean_item)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.auto_print, self.timer)
        self.timer.Start(100)

        menu_bar = wx.MenuBar()
        about_menu = wx.Menu()
        about_menu.Append(wx.ID_ABOUT, "关于")
        self.Bind(wx.EVT_MENU, self.start_about, id=wx.ID_ABOUT)
        menu_bar.Append(about_menu, "关于软件")
        self.SetMenuBar(menu_bar)
    def simplify_string(self, input_string):
        output_string = ""
        count = 0
        for char in input_string:
            if char == '%':
                count += 1
            else:
                if count % 2 == 0:
                    output_string += '%' * (count // 2)
                else:
                    output_string += '%' * ((count - 1) // 2) + char
                count = 0

        # 处理最后一组连续的百分号
        if count % 2 == 0:
            output_string += '%' * (count // 2)
        else:
            output_string += '%' * ((count - 1) // 2)

        return output_string

    def auto_print(self,event):
        self.编辑框5.SetValue(json.dumps(ast.literal_eval(str(text_json)), ensure_ascii=False))

    def start_about(self,event):
        message = wx.MessageDialog(None, caption="about", message="程序设计:daijunhao\n感谢你使用此程序!", style=wx.OK | wx.ICON_INFORMATION)
        if message.ShowModal() == wx.ID_OK:
            pass

    def flushed_print(self):
        self.编辑框10.SetLabel("")
        for i in range(len(text_json['rawtext'])):
            if 'text' in text_json['rawtext'][i]:
                self.编辑框10.AppendText(f"{text_json['rawtext'][i]['text']}")
            if 'score' in text_json['rawtext'][i]:
                self.编辑框10.AppendText(f"[计分板显示,计分板玩家名称/类型:{text_json['rawtext'][i]['score']['name']},计分板名称:{text_json['rawtext'][i]['score']['objective']}]")
            if 'selector' in text_json['rawtext'][i]:
                self.编辑框10.AppendText(f"[选择器类型,选择器玩家类型:{text_json['rawtext'][i]['selector']}]")
            try:
                text_json['rawtext'][i]['with']
            except KeyError:
                if 'translate' in text_json['rawtext'][i]:
                    self.编辑框10.AppendText(f"{text_json['rawtext'][i]['translate']}")
            try:
                text_json['rawtext'][i]['translate']
            except KeyError:
                if 'with' in text_json['rawtext'][i]:
                    self.编辑框10.AppendText("")
            if 'with' in text_json['rawtext'][i] and 'translate' in text_json['rawtext'][i]:
                text_ok = text_json['rawtext'][i]['translate']
                text_count = text_ok.count("%%s")
                for j in range(text_count):
                    try:
                        text_ok = text_ok.replace("%%s", text_json['rawtext'][i]['with'][j], 1)
                    except IndexError:
                        text_ok = text_ok.replace("%%s", "", 1)
                numbers_find = re.findall(r'%%(\d+)', text_ok)  # 匹配所有以 %% 开头的数字部分
                for f in range(len(numbers_find)):
                    try:
                        print(numbers_find[f])
                        text_ok = text_ok.replace(f"%%{numbers_find[f]}",text_json['rawtext'][i]['with'][int(numbers_find[f])-1])
                    except IndexError:
                        text_ok = text_ok.replace(f"%%{numbers_find[f]}", f"%{numbers_find[f]}")
                matches = re.findall(r"%+", text_ok)
                for k in range(len(matches)):
                    sk = self.simplify_string(matches[k])
                    text_ok = text_ok.replace(f"{matches[k]}",sk)
                self.编辑框10.AppendText(text_ok)

    def flushed_ok(self):
        self.data = []
        self.超级列表框1.DeleteAllItems()
        for i in range(len(text_json['rawtext'])):
            if 'text' in text_json['rawtext'][i]:
                self.data.append({'one': i+1, 'two': f"文本类型,文本内容:{text_json['rawtext'][i]['text']}"})
            if 'score' in text_json['rawtext'][i]:
                self.data.append({'one': i + 1, 'two': f"计分板类型,计分板玩家名称/类型:{text_json['rawtext'][i]['score']['name']},计分板名称:{text_json['rawtext'][i]['score']['objective']}"})
            if 'selector' in text_json['rawtext'][i]:
                self.data.append({'one': i + 1, 'two': f"选择器类型,选择器玩家类型:{text_json['rawtext'][i]['selector']}"})
            try:
                text_json['rawtext'][i]['with']
            except KeyError:
                if 'translate' in text_json['rawtext'][i]:
                    self.data.append({'one': i + 1, 'two': f"变量文本类型(只有文本),文本内容:{text_json['rawtext'][i]['translate']}"})
            try:
                text_json['rawtext'][i]['translate']
            except KeyError:
                if 'with' in text_json['rawtext'][i]:
                    self.data.append({'one': i + 1, 'two': f"变量文本类型(只有变量,输出为空),变量内容:{';'.join(text_json['rawtext'][i]['with'])}"})
            if 'with' in text_json['rawtext'][i] and 'translate' in text_json['rawtext'][i]:
                self.data.append({'one': i + 1, 'two': f"变量文本类型,变量内容:{';'.join(text_json['rawtext'][i]['with'])},文本内容:{text_json['rawtext'][i]['translate']}"})
        self.超级列表框1.AddObjects(self.data)
        self.flushed_print()

    def on_right_click(self,event):
        pos = wx.GetMousePosition()
        pos = self.ScreenToClient(pos)

        self.PopupMenu(self.popup_menu, pos)

    def add_text_按钮被单击(self,event):
        if self.add_text.GetLabel() == "修改":
            try:
                text_json['rawtext'][self.超级列表框1.GetFirstSelected()] = {"text": f"{self.text_text.GetValue()}"}
                self.add_text.SetLabel("添加文本")
                self.flushed_ok()
            except IndexError:
                self.add_text.SetLabel("添加文本")
        elif self.add_text.GetLabel() == "添加文本":
            text_json['rawtext'].append({"text":f"{self.text_text.GetValue()}"})
            self.flushed_ok()

    def clean_item_everyone(self,event):
        message = wx.MessageDialog(None, caption="警告", message="你确定要清空列表?", style=wx.YES_NO | wx.ICON_WARNING)
        if message.ShowModal() == wx.ID_YES:
            text_json['rawtext'].clear()
            self.flushed_ok()

    def add_selector_按钮被单击(self,event):
        if self.add_selector.GetLabel() == "修改":
            try:
                text_json['rawtext'][self.超级列表框1.GetFirstSelected()] = {"selector": f"{self.selector_text.GetValue()}"}
                self.add_selector.SetLabel("添加选择器")
                self.flushed_ok()
            except IndexError:
                self.add_selector.SetLabel("添加选择器")
        elif self.add_selector.GetLabel() == "添加选择器":
            text_json['rawtext'].append({"selector": f"{self.selector_text.GetValue()}"})
            self.flushed_ok()

    def add_score_按钮被单击(self,event):
        if self.add_score.GetLabel() == "修改":
            try:
                text_json["rawtext"][self.超级列表框1.GetFirstSelected()] = {"score":{"name":f"{self.score_selector.GetValue()}", "objective":f"{self.score_name.GetValue()}"}}
                self.add_score.SetLabel("添加计分板")
                self.flushed_ok()
            except IndexError:
                self.add_score.SetLabel("添加计分板")
        elif self.add_score.GetLabel() == "添加计分板":
            text_json["rawtext"].append({"score": {"name": f"{self.score_selector.GetValue()}", "objective": f"{self.score_name.GetValue()}"}})
            self.flushed_ok()

    def generate_json_按钮被单击(self,event):
        self.编辑框5.SetValue(json.dumps(ast.literal_eval(str(text_json)), ensure_ascii=False))
        self.flushed_ok()


    def copy_json_按钮被单击(self,event):
        pycopy.copy(f"{self.编辑框5.GetValue()}")
        self.flushed_ok()


    def delete_content_按钮被单击(self,event):
        try:
            text_json["rawtext"].remove(text_json["rawtext"][self.超级列表框1.GetFirstSelected()])
        except IndexError:
            message = wx.MessageDialog(None, caption="Error", message=f"删除失败", style=wx.OK | wx.ICON_ERROR)
            if message.ShowModal() == wx.ID_OK:
                pass
        self.flushed_ok()


    def revise_json_按钮被单击(self,event):
        if 'text' in text_json['rawtext'][self.超级列表框1.GetFirstSelected()]:
            self.text_text.SetLabel(f"{text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['text']}")
            self.add_text.SetLabel("修改")
            self.add_selector.SetLabel("添加选择器")
            self.add_score.SetLabel("添加计分板")
            self.add_path_text.SetLabel("添加文本")
        if 'score' in text_json['rawtext'][self.超级列表框1.GetFirstSelected()]:
            self.score_selector.SetLabel(f"{text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['score']['name']}")
            self.score_name.SetLabel(f"{text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['score']['objective']}")
            self.add_score.SetLabel("修改")
            self.add_text.SetLabel("添加文本")
            self.add_selector.SetLabel("添加选择器")
            self.add_path_text.SetLabel("添加文本")
        if 'selector' in text_json['rawtext'][self.超级列表框1.GetFirstSelected()]:
            self.selector_text.SetLabel(f"{text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['selector']}")
            self.add_selector.SetLabel("修改")
            self.add_text.SetLabel("添加文本")
            self.add_score.SetLabel("添加计分板")
            self.add_path_text.SetLabel("添加文本")
        try:
            text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['with']
        except KeyError:
            if 'translate' in text_json['rawtext'][self.超级列表框1.GetFirstSelected()]:
                self.text_text_1.SetLabel(f"{text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['translate']}")
                self.add_selector.SetLabel("添加选择器")
                self.add_text.SetLabel("添加文本")
                self.add_score.SetLabel("添加计分板")
                self.add_path_text.SetLabel("修改")
        try:
            text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['translate']
        except KeyError:
            if 'with' in text_json['rawtext'][self.超级列表框1.GetFirstSelected()]:
                self.path_content.SetLabel(f"{';'.join(text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['with'])}")
                self.add_selector.SetLabel("添加选择器")
                self.add_text.SetLabel("添加文本")
                self.add_score.SetLabel("添加计分板")
                self.add_path_text.SetLabel("修改")
        if 'with' in text_json['rawtext'][self.超级列表框1.GetFirstSelected()] and 'translate' in text_json['rawtext'][self.超级列表框1.GetFirstSelected()]:
            self.path_content.SetLabel(f"{';'.join(text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['with'])}")
            self.text_text_1.SetLabel(f"{text_json['rawtext'][self.超级列表框1.GetFirstSelected()]['translate']}")
            self.add_selector.SetLabel("添加选择器")
            self.add_text.SetLabel("添加文本")
            self.add_score.SetLabel("添加计分板")
            self.add_path_text.SetLabel("修改")



    def read_json_按钮被单击(self,event):
        global text_json
        try:
            text_json = json.loads(self.编辑框6.GetValue())
            message = wx.MessageDialog(None, caption="info", message=f"读取json成功", style=wx.OK | wx.ICON_INFORMATION)
            if message.ShowModal() == wx.ID_OK:
                pass
            self.flushed_ok()
        except json.decoder.JSONDecodeError:
            message = wx.MessageDialog(None, caption="Error",message=f"json解码错误",style=wx.OK | wx.ICON_ERROR)
            if message.ShowModal() == wx.ID_OK:
                pass
            self.flushed_ok()

    def flushed_content_按钮被单击(self,event):
        self.flushed_ok()


    def add_path_text_按钮被单击(self,event):
        if self.add_path_text.GetLabel() == "修改":
            try:
                text_json["rawtext"][self.超级列表框1.GetFirstSelected()] = {"with":str(self.path_content.GetValue()).split(";"),"translate":f"{self.text_text_1.GetValue()}"}
            except IndexError:
                self.add_path_text.SetLabel("添加文本")
            self.add_path_text.SetLabel("添加文本")
            self.flushed_ok()
        elif self.add_path_text.GetLabel() == "添加文本":
            text_json["rawtext"].append({"with":str(self.path_content.GetValue()).split(";"),"translate":f"{self.text_text_1.GetValue()}"})
            self.flushed_ok()

class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()