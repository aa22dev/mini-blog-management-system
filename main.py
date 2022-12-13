import config
import components.dashboard as dash
import components.demo as demo

if __name__ == '__main__':
    dem = demo.demo()
    dem.make()
    d = dash.dashboard()
    d.mainMenu()
