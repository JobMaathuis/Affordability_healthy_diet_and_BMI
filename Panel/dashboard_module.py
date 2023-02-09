#!/usr/bin/python3

import panel as pn


class Dashboard:
    '''
    This class creates a panel dashboard to which pages can be added
    
    Arguments: 
    title (str): title of the dashboard
    header_color (str): name of a color or hex color code
    css (str): raw css
    
    Returns:    
    dashboard object
    
    Author(s): 
    Job Maathuis
    '''
    
    
    def __init__(self, title: str, header_color: str, css):
        # initialise dashboard
        self.dashboard = pn.template.BootstrapTemplate(title=title, header_background=header_color, sidebar_width=200)
        self.dashboard.main.extend([pn.pane.Markdown(''), pn.Column(width=1500)]) 
        self.main_page = self.dashboard.main[1]
        pn.extension(raw_css=[css])
        
        # variable to save all the pages
        self.pages = {}
        
        
    def add_page(self, title: str, show_page: bool, *contents):
        ''' 
        Adds a page to the dashboards and create a sidebar navigation button for it 
        
        Arguments:
        title      (str): title of the page
        show_page (bool): boolean to show the page when showing the dahsboard (if more pages have this as True the last page added will be shown)
        contents        : contents to be added to the page
        
        Returns:
        None
        '''
        sidebar_button = pn.widgets.Button(name=title, width=150)  # create sidebar button
        self.dashboard.sidebar.append(sidebar_button)  # append button to sidebar
        sidebar_button.on_click(self._update_page)  # callback
        self.pages[title] = [*contents]  # add the contents to the page dictionary
        if show_page:
            self._show_page(title)
    
    
    def _update_page(self, event):
        '''
        Private callback method to update the page when a sidebar button is clicked 
          
        Arguments:
        event (object): widget cacllback event
        
        Returns:
        None
        '''
        name = event.obj.name  # extract name from event
        self.main_page.clear()  # clear the main page
        self.main_page.append(pn.pane.Markdown(f'##{name}'))  # create title
        self.main_page.extend([item for item in self.pages[name]])  # add all of the contents to the page
        
        # make right button active:
        self._make_button_active(name)
        
    
    def add_tabs_to_page(self, page_title: str, *tab_contents: dict):
        ''' 
        Adds tabs to a specific page, with tab contents.
        
        Arguments:
        page_title       (str): title of the page where the tabs need to be added
        tab_contents (dict(s)): dict or multiple dicts, where each dict key is the name of the tab
                                and each value a list with contents 
        
        Returns:
        None
        '''
        # create a tab object
        tabs = pn.Tabs()
        
        # add each of the contents to the tab object
        for tab_content in tab_contents:
            for tab_title, contents in tab_content.items():
                tabs.append((tab_title, pn.Column(*contents)))
        
        # add tab object to the right page
        self.pages[page_title].append(tabs)
        
    
    def _show_page(self, title: str):
        '''
        Private method that show the page of the given page title 
        
        Arguments:
        title (str): title of the page
        
        Returns:
        None
        '''
        self.main_page.clear()
        self.main_page.append(pn.pane.Markdown(f'##{title}'))
        self.main_page.extend([item for item in self.pages[title]])
        self._make_button_active(title)
            
    def _make_button_active(self, title: str):
        '''
        Private method that updates the css classes of each button
        so that the user knows which page he currently visits
        
        Arguments:
        title (str): title of the page
        
        Returns:
        None
        '''
        
        for button in self.dashboard.sidebar:
            # update css class to active
            if button.name == title:
                button.css_classes = ['sidebar_button']
            # reset all other buttons to not have any css
            else:
                button.css_classes = []
    
    def show(self):
        '''Shows the dashboard''' 
        self.dashboard.show()
    