from views.report import Report as ReportView


class ReportController:

    def __init__(self):
        self.reportView = ReportView()
        self.reportView.displayTitle()
