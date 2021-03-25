"""
This code was helpful,
https://stackoverflow.com/questions/32141623/pyqt5-and-asyncio-yield-from-never-finishes
"""
import os
import sys
import quamash
import asyncio
import traceback
import PyQt5
import pdb
import math
import moteus

# Required setup to get event loop working
app = PyQt5.QtWidgets.QApplication(sys.argv)
loop = quamash.QEventLoop(app)
asyncio.set_event_loop(loop)
loop.set_debug(True)  # optional


# Select QT5
# https://github.com/enthought/traitsui/issues/407
os.environ["ETS_TOOLKIT"] = "qt"
os.environ["QT_API"] = "pyqt5"
from traits.api import HasTraits, Button, Instance, Int, Bool
from traitsui.api import ModelView, View, Item, Label
from PyQt5.QtCore import pyqtRemoveInputHook

pyqtRemoveInputHook()  # enabled pdb.set_trace()    ????


class App(HasTraits):
    """ Traits application model.
    """
    global a    ###variable du slidr 1 pour (v)
    a = 5
    global b    ####variable du slier 2 pour (mt)
    b = 6
    
    global c    ####"variable du slider pour (sp)
    c = 7
    running = Bool(False)

    async def test_task(self, event):
        while not event.is_set():
            loop = asyncio.get_event_loop()
            print("START")
            await asyncio.sleep(0.02, loop)


    async def test_task2(self):



        while True:
                   
           loop = asyncio.get_event_loop()
           self.running = True
           print(a,b,c)  #commande pour faire actioer position et retour indfo console 
           await asyncio.sleep(0.02, loop)

           self.running = False

class AppView(ModelView):
    """Traits application view."""

    model = Instance(App)

    test_task_btn = Button("START1")
    test_task_btn2 = Button("STOP1andSTART2")

    event = asyncio.Event()

    def _test_task_btn_fired(self):
        print("Button pressed.")
        try:
            loop.create_task(self.model.test_task(self.event))
        except:
            traceback.print_exc()
            print("Problem")

    def _test_task_btn2_fired(self):
        print("Button2 pressed.")
        self.event.set()
        try:
            loop.create_task(self.model.test_task2())
        except:
            traceback.print_exc()
            print("Problem")

    def default_traits_view(self):
        view = View(
            Label("TesterLite"),
            Item("test_task_btn", show_label=False),
            Item("test_task_btn2", show_label=False),
            resizable=True,
            title="MoteusControllerTesterLite",
            height=400,
            width=400,
        )
        return view

with loop:
    print("Launching app.")
    model = App()
    view = AppView(model=model)
    view.edit_traits()
    print("edit_traits")
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8:
        asyncio.events._set_running_loop(loop)  # Need if using >= Python 3.8


    loop.run_forever()


    print("Finished run_forever()")
print("App closed.")




