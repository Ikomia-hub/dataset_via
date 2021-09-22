from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class IkomiaPlugin(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        from dataset_via.dataset_via_process import DatasetViaFactory
        # Instantiate process object
        return DatasetViaFactory()

    def getWidgetFactory(self):
        from dataset_via.dataset_via_widget import DatasetViaWidgetFactory
        # Instantiate associated widget object
        return DatasetViaWidgetFactory()
