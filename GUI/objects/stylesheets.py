"""
In this module are the style sheets used by the program objects.
"""

stylesheet_widget = u"""
.widget{
    background-color: rgb(7, 7, 7);
}"""

stylesheet_display = u"""
.display{
    border: 1px solid; 
    border-color: rgb(7,7,7);
    border-radius: 3px;
    background-color: rgb(111, 111, 0);
    color:#000;}
.display::placeholder{
    color: #000;
}
"""

stylesheet_btn_numbers = u"""
.btn{
    border: 1px solid; 
    border-color: rgb(198, 198, 148); 
    background-color: rgb(45,45, 45); 
    border-radius: 2px; color: #fff;
}
.btn:pressed{
    background-color: rgb(25, 25, 25); 
    border: 2px solid;
    border-color: rgb(198, 198, 148);
    border-radius: 2px;
}"""

stylesheet_btn_operators = """
.btn{
    border: 1px solid; 
    border-color: rgb(136, 136, 101); 
    background-color: rgb(25, 25, 25); 
    border-radius: 2px; 
    color: #fff;
}
.btn:pressed{
    background-color: 
    rgb(10, 10, 10); 
    border: 2px solid;
    border-color: rgb(136, 136, 101);
    border-radius: 2px;
}"""

stylesheet_btn_del = """
.btn{
    background-color: rgb(255, 5, 9);
    color: white;
    border: 1px solid;
    border-color: rgb(198, 198, 148);
    border-radius: 2px;
}
.btn:pressed{
    background-color: rgb(213, 4, 8);
    border: 2px solid;
    border-color: rgb(198, 198, 148);
    border-radius: 2px;
}"""

