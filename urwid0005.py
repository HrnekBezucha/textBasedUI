#!/usr/bin/python3
'''
Desc: Program asks simple question, user simply answer.
Source: http://urwid.org/tutorial/index.html#question-and-answer
'''
import urwid

def exit_on_q(key):
  if key in ('q', 'Q'):
    raise urwid.ExitMainLoop()

class QuestionBox(urwid.Filler):
  def keypress(self, size, key):
    if key != 'enter':
      return super(QuestionBox, self).keypress(size, key)
    self.original_widget = urwid.Text(
      u'Nice to meet you, \n%s \nPress Q to exit.' % edit.edit_text)

edit = urwid.Edit(u'What is your name?\n')
fill = QuestionBox(edit)
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()
