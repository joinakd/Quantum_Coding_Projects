import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
import numpy as np
import tkinter
from tkinter import DISABLED, NORMAL, LEFT, END
import warnings

warnings.filterwarnings('ignore')

# Define Window
root = tkinter.Tk()
root.title('Quantum Feel')

#set the icon
# root.iconbitmap(default="logo.ico") # works for windows logo
root.iconbitmap('@logo.xbm') #for linux systems
root.geometry('410x350')
root.resizable(0,0) # Blocking the resize feature

# Define the colors and fonds
background = '#2c94c8'
# buttons = '#834558'
buttons = '#eab676'
special_buttons = ('Inter Semi Bold',18)
display_font = ('Inter Semi Bold',32)

# Define the Frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both',expand=True)

# Define the Display Frame Layout
display = tkinter.Entry(display_frame,width=120,font = display_font,bg=background,borderwidth=10,justify=LEFT)
display.pack(padx=3,pady=4)


# Define Functions
def display_gate(gate_input):
    """
    Adds a corresponding gate notation in the display to track the operations.
    If the number of operation reach ten, all gate buttons are disabled
    """
    # Insert the defined gate
    display.insert(END,gate_input)

    #Check if the number of operations has reached ten, if yes,
    #disable all the gate buttons
    input_gates = display.get()
    num_gates_pressed = len(input_gates)
    list_input_gates = list(input_gates)
    search_word = ["R","D"]
    count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
    num_gates_pressed -= sum(count_double_valued_gates)
    if num_gates_pressed == 10:
        gates = [x_gate,y_gate,z_gate,Rx_gate,Ry_gate,Rz_gate, s_gate,sd_gate,t_gate,td_gate,hadamard]
        for gate in gates:
            gate.config(state=DISABLED)

def clear (circuit):
    """
    Clears the display!
    Reinitializes the Quantum Circuit for fresh calculation!
    Checks if the gate buttons are dissabled, if so, enable the buttons
    """
    
    # Clear the display
    display.delete(0,END)

    #reset the circuit to initial state |0>
    initialize_circuit()

    # Check if the buttons are dissabled and if so, enable them
    if x_gate['state']==DISABLED:
        gates = [x_gate,y_gate,z_gate,Rx_gate,Ry_gate,Rz_gate, s_gate,sd_gate,t_gate,td_gate,hadamard]
        for gate in gates:
            gate.config(state=NORMAL)


# Initialize the Quantum Circuit
def initialize_circuit():
    """
    Initializes the Quantum Circuit
    """
    global circuit
    circuit = QuantumCircuit(1)

initialize_circuit()
theta = 0

def change_theta(num,window,circuit,key):
    """
    Changes the global variable theta and destroys the window
    """
    global theta 
    theta = num*(np.pi)
    if key=='x':
        circuit.rx(theta,0)
        theta=0
    elif key=='y':
        circuit.ry(theta,0)
        theta=0
    else:
        circuit.rz(theta,0)
        theta=0
    window.destroy()

def user_input(circuit,key):
    """
    Take the user input for rotation angle for parameterized 
    Rotation gates Rx, Ry, Rz.
    """

    # Initialize and define the properties of window
    get_input = tkinter.Tk()
    get_input.title('Get Theta')
    get_input.geometry('320x170')
    get_input.resizable(0,0)

    val1 = tkinter.Button(get_input,height=2,width=4,font=("Inter Semi Bold",10),bg=buttons,text='PI/4',command=lambda:change_theta(0.25,get_input,circuit,key))
    val1.grid(row=0,column=0)

    val2 = tkinter.Button(get_input,height=2,width=4,font=("Inter Semi Bold",10),bg=buttons,text='PI/2',command=lambda:change_theta(0.50,get_input,circuit,key))
    val2.grid(row=0,column=1)

    val3 = tkinter.Button(get_input,height=2,width=4,font=("Inter Semi Bold",10),bg=buttons,text='PI',command=lambda:change_theta(1.0,get_input,circuit,key))
    val3.grid(row=0,column=2)

    val4 = tkinter.Button(get_input,height=2,width=4,font=("Inter Semi Bold",10),bg=buttons,text='2*PI',command=lambda:change_theta(2.0,get_input,circuit,key))
    val4.grid(row=0,column=3)

    nval1 = tkinter.Button(get_input,height=2,width=4,font=("Inter Semi Bold",10),bg=buttons,text='-PI/4',command=lambda:change_theta(-0.25,get_input,circuit,key))
    nval1.grid(row=1,column=0)

    nval2 = tkinter.Button(get_input,height=2,width=4,font=("Inter Semi Bold",10),bg=buttons,text='-PI/2',command=lambda:change_theta(-0.50,get_input,circuit,key))
    nval2.grid(row=1,column=1)

    nval3 = tkinter.Button(get_input,height=2,width=4,font=("Inter Semi Bold",10),bg=buttons,text='-PI',command=lambda:change_theta(-1.0,get_input,circuit,key))
    nval3.grid(row=1,column=2)

    nval4 = tkinter.Button(get_input,height=2,width=4,font=("Inter Semi Bold",10),bg=buttons,text='-2*PI',command=lambda:change_theta(-2.0,get_input,circuit,key))
    nval4.grid(row=1,column=3)

    text_object = tkinter.Text(get_input,height=20,width=20,bg="light cyan")

    note="""
    GIVE THE VALUE FOR THETA

    The value has the range [-2*PI, 2*PI]
    """

    text_object.grid(sticky="WE",columnspan=4)
    text_object.insert(END,note)

    get_input.mainloop()

def visualize_circuit(circuit,window):
    """
    Visualizes the single qubit rotations corresponding to applied gates in a seperate tkinter window
    Handles any possible visualization error
    """

    try: 
        visualize_transition(circuit=circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()

def about():
    """
    Displays the info about the project!!
    """
    info = tkinter.Tk()
    info.title('About')
    
    info.geometry('650x470')
    info.resizable(0,0)

    text = tkinter.Text(info,height=20,width=20)

    #Create label
    label = tkinter.Label(info,text= "About Quantum Feel:")
    label.config(font=("Inter Semi Bold",20))

    text_to_display="""
    About Visualization tool for Single Qubit Rotation on Bloch Sphere 
    
    Created by: Akash Dhingra with help from Jay Shah
    Created using: Python, Tkinter, Qiskit

    Info about the gate buttons and corresponding qiskit commands:

    X = flips the state of qubit -                                  circuit.x()
    Y = rotates the state vector about Y-axis -                     circuit.y()
    Z = flips the phase by PI radians -                             circuit.z ()
    Rx parameterized rotation about the X axis -                    circuit.rx ()
    Ry = parameterized rotation about the Y axis -                  circuit.ry()
    Rz parameterized rotation about the Z axis-                     circuit.rz ()
    S = rotates the state vector about Z axis by PI/2 radians -     circuit.s()
    T = rotates the state vector about Z axis by PI/4 radians -     circuit.t()
    Sd = rotates the state vector about Z axis by -PI/2 radians -   circuit.sdg ()
    Td = rotates the state vector about Z axis by -PI/4 radians -   circuit.tdg()
    H = creates the state of superposition -                        circuit.h()
    
    For Rx, Ry and Rz, 
    theta (rotation_angle) allowed range in the app is [-2*PI, 2*PI]

    In case of a Visualization Error, the app closes automatically. 
    This indicates that visualization of your circuit is not possible.
    At a time, only ten operations can be visualized.
    
    """
    label.pack()
    text.pack(fill='both',expand=True)

    # Insert the text
    text.insert(END,text_to_display)

    #run
    info.mainloop()


# Define the first row of buttons
x_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='X',command=lambda:[display_gate('X'),circuit.x(0)])
y_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='Y',command=lambda:[display_gate('Y'),circuit.y(0)])
z_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='Z',command=lambda:[display_gate('Z'),circuit.z(0)])

x_gate.grid(row=0,column=0,sticky='WE',ipadx=45,pady=1)
y_gate.grid(row=0,column=1,sticky='WE',ipadx=45,pady=1)
z_gate.grid(row=0,column=2,sticky='WE',ipadx=45,pady=1)

#Define the second row of buttons
Rx_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='RX',command=lambda:[display_gate('Rx'),user_input(circuit,'x')])
Ry_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='RY',command=lambda:[display_gate('Ry'),user_input(circuit,'y')])
Rz_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='RZ',command=lambda:[display_gate('Rz'),user_input(circuit,'z')])

Rx_gate.grid(row=1,column=0,columnspan=1,sticky='WE',pady=1)
Ry_gate.grid(row=1,column=1,columnspan=1,sticky='WE',pady=1)
Rz_gate.grid(row=1,column=2,columnspan=1,sticky='WE',pady=1)

# Define the third row of buttons
s_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='S',command=lambda:[display_gate('s'),circuit.s(0)])
sd_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='SD',command=lambda:[display_gate('SD'),circuit.sdg(0)])
hadamard = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='H',command=lambda:[display_gate('H'),circuit.h(0)])

s_gate.grid(row=2,column=0,columnspan=1,sticky='WE',pady=1)
sd_gate.grid(row=2,column=1,sticky='WE',pady=1)
hadamard.grid(row=2,column=2,rowspan=2,sticky='WNSE',pady=1)

# Define the fifth row of buttons
t_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='T',command=lambda:[display_gate('t'),circuit.t(0)])
td_gate = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='TD',command=lambda:[display_gate('TD'),circuit.tdg(0)])

t_gate.grid(row=3,column=0,sticky='WE',pady=1)
td_gate.grid(row=3,column=1,sticky='WE',pady=1)

# Define the Quit and Visualize buttons
quit = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='Quit',command=root.destroy)
visualize = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='Visualize',command=lambda:visualize_circuit(circuit,root))

quit.grid(row=4,column=0,columnspan=2,sticky='WE',ipadx=5,pady=1)
visualize.grid(row=4,column=2,columnspan=1,sticky='WE',ipadx=8,pady=1)

# Define the clear button
clear_button = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='Clear',command=lambda:clear(circuit))
clear_button.grid(row=5,column=0,columnspan=3,sticky='WE')

# Define the about button
about_button = tkinter.Button(button_frame,font=button_frame,bg=buttons,text='About',command=about)
about_button.grid(row=6,column=0,columnspan=3,sticky='WE')



# Run the main loop
root.mainloop()




