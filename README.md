## Initial configuration

- Goal: setup and run the project

### Software to install

#### MacOs

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Pyhton 3.9.10](https://www.python.org/downloads/release/python-3910/)
- [ffmpeg 5.0.1](https://evermeet.cx/ffmpeg/)
- Pip 3
  - `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
  - `python3 get-pip.py`
  - `pip3 --version`, verify the version shows up
- Virtualenv
  - `pip install virtualenv`

#### Linux

- `sudo apt-get install git -y`
- `sudo apt-get install python3.9 -y`
- `sudo apt-get install python3-pip -y`
- `sudo apt-get install python3-venv -y`
- `sudo apt-get install ffmpeg -y`

#### Configuration

- Clone the respository

  - `git clone https://github.com/manu-yaff/Tesina`

- Checkout to the correct branch

  - `git checkout visualization-tool`

- Navigate to the folder 'Tesina'

  - `cd Tesina`

- Create a virtual environment

  - `python3 -m venv .venv`

- Activate the virtual environment

  - `source .venv/bin/activate`

- Install the required [packages](./requirements.txt)

  - `pip3 install -r requirements.txt`

- Navigate to the folder 'vis_tool'

  - `cd vis_tool`

- Execute

  - `./manage.py migrate`

- Execute

  - `./manage.py runserver`

- You should a similar message in your terminal:

  ```
  Starting the development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK
  ```

- Open your browser in the url: http://127.0.0.1:8000/
