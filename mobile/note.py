#!python2
# coding:utf-8

import appex
import console
import evernote.edam.type.ttypes as Types
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
from html2text import html2text

auth_token = "S=s128"
NOTEBOOK_NAME = '书籍相关'
book_list = ['西方哲学史', '书籍笔记', '备用']

def main():
    console.clear()

    # 获取笔记标题
    i = console.alert('请选择', '', book_list[0], book_list[1], book_list[2], False)
    note_title = book_list[i - 1]

    # 获取选中的文字内容
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    text = appex.get_text()
    if not text:
        print('No text input found.')
        return
    content_to_add = str(html2text(text))

    client = EvernoteClient(token=auth_token, sandbox=False)
    note_store = client.get_note_store()
    # # 由笔记本名称获取笔记本的 guid
    # 直接根据笔记名称搜索更快，故略去
    # notebooks = note_store.listNotebooks()
    # # print "Found ", len(notebooks), " notebooks:"
    # for notebook in notebooks:
    #     if notebook.name == NOTEBOOK_NAME:
    #         notebook_guid = notebook.guid
    #         # print "notebook:   ", notebook.name

    # 根据笔记名称在指定笔记本中搜索
    filter = NoteStore.NoteFilter()
    filter.words = "title:" + note_title
    #filter.notebookGuid = notebook_guid

    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = True

    ourNoteList = note_store.findNotesMetadata(auth_token, filter, 0, 1, spec)

    # 如笔记存在，则将内容添加到笔记末尾
    if len(ourNoteList.notes) != 0:
        whole_note = note_store.getNote(auth_token, ourNoteList.notes[0].guid, 1, 0, 0, 0)
        note_content = whole_note.content.replace('</en-note>',
                                                  '<div><br/></div><div>' + content_to_add + '</div></en-note>')
        whole_note.content = note_content
        note_store.updateNote(whole_note)
    else:
        # 如笔记不存在，则在指定笔记本中新建笔记
        note = Types.Note()
        note.title = note_title
        # note.notebookGuid = notebook_guid
        note.content = '<?xml version="1.0" encoding="UTF-8"?>'
        note.content += '<!DOCTYPE en-note SYSTEM ' \
                        '"http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note>%s<br/></en-note>' % content_to_add
        note_store.createNote(auth_token, note)

    print "Add note success!"
    return


if __name__ == '__main__':
    main()