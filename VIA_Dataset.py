from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class VIA_Dataset(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        from VIA_Dataset.VIA_Dataset_process import VIA_DatasetProcessFactory
        # Instantiate process object
        return VIA_DatasetProcessFactory()

    def getWidgetFactory(self):
        from VIA_Dataset.VIA_Dataset_widget import VIA_DatasetWidgetFactory
        # Instantiate associated widget object
        return VIA_DatasetWidgetFactory()
