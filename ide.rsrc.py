{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':u'nPyIDE',
          'size':(745, 548),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuFile',
             'label':u'File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileNew',
                   'label':u'&New\tCtrl+N',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'Call', 
    'position':(490, 42), 
    'size':(101, -1), 
    'label':'Call', 
    },

{'type':'StaticBox', 
    'name':'moduletools', 
    'position':(481, 28), 
    'size':(120, 157), 
    'label':'Tools', 
    },

{'type':'StaticText', 
    'name':'modules', 
    'position':(333, 2), 
    'text':'Modules (.pyc must exist)', 
    },

{'type':'List', 
    'name':'List1', 
    'position':(330, 15), 
    'size':(138, 466), 
    'items':[], 
    },

{'type':'Button', 
    'name':'Run', 
    'position':(147, 141), 
    'size':(112, -1), 
    'label':'Run', 
    },

{'type':'Button', 
    'name':'Duplicate', 
    'position':(147, 109), 
    'size':(112, -1), 
    'label':'Duplicate', 
    },

{'type':'Button', 
    'name':'Delete', 
    'position':(147, 77), 
    'size':(112, -1), 
    'label':'Delete', 
    },

{'type':'StaticBox', 
    'name':'Tools', 
    'position':(139, 29), 
    'size':(128, 149), 
    'label':'Tools', 
    },

{'type':'Button', 
    'name':'Open', 
    'position':(147, 46), 
    'size':(112, -1), 
    'label':'Open', 
    },

{'type':'StaticText', 
    'name':'Files', 
    'position':(7, 1), 
    'text':'Files', 
    },

{'type':'List', 
    'name':'files', 
    'position':(5, 15), 
    'size':(-1, 467), 
    'items':[], 
    },

] # end components
} # end background
] # end backgrounds
} }
