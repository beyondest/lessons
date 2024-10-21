# Useful tips for VSCode

## Shortcuts

- Reopen closed tab: ``Ctrl + Shift + T``

### Terminal and Code Execution
- `Ctrl + U`: Maximize terminal
- `Ctrl + Alt + N`: Run code
- `Ctrl + Alt + M`: Stop running code
- `Ctrl + Alt + L`: Run code in interactive mode
- `Ctrl + Alt + Enter`: Run single unit in `.ipynb`

### Navigation and Editor Controls
- `Ctrl + +`: Increase code size
- `Ctrl + Alt + Z`: Go to definition
- `Ctrl + P`: Fold all code blocks
- `Ctrl + L`: Unfold all code blocks
- `Ctrl + 0`: Focus on Explorer
- `Ctrl + ```: Focus on Terminal
- `Ctrl + 1`: Focus on Editor
- `Ctrl + Fn + Up Arrow / Down Arrow`: Focus on text bar and change text
- `Ctrl + Fn + Left Arrow / Right Arrow`: Jump to beginning/end of the editor

### File Explorer Controls
- `Left Arrow`: Fold current folder in Explorer
- `Ctrl + Left Arrow`: Fold all folders in Explorer

### Terminal Management
- `Ctrl + Shift + Delete`: Kill active terminal

### CMake and Ninja Commands
- `Ctrl + T`: Run `cmake -GNinja ..`
- `Ctrl + W`: Run Ninja without executing code
- `Ctrl + R`: Run `openocd` using `workspaceFolder/openocd.cfg`, with GDB port 5000

## Keyboard Bindings Setup
To set custom keybindings in `keyboardbindings.json`, make sure to use the correct tasks:
- `-runtask` is invalid
- `runtask` is valid
