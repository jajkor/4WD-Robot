import cv2
import os
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk

class GUI_App:

	def __init__(self, stream_url):
		self.stream_url = stream_url
		self.cap = cv2.VideoCapture(stream_url)

		self.root = Tk()
		self.root.wm_title("ESP32-CAM VIDEO STREAM")

		width = self.root.winfo_screenwidth()
		height = self.root.winfo_screenheight()
		self.root.geometry("%dx%d" % (width, height))

		frame = Frame(self.root)
		frame.pack()

		self.feed_label = Label(self.root)
		self.feed_label.pack(side=LEFT)

		self.start_button = Button(self.root, text='Start Recording', command=self.start_recording)
		self.start_button.pack(side=RIGHT)

		self.stop_button = Button(self.root, text='Stop Recording', command=self.stop_recording, state=DISABLED)
		self.stop_button.pack(side=RIGHT)

		self.recording = False
		self.video_writer = None

		self.capture_button = Button(self.root, text='Capture', command=self.capture_image)
		self.capture_button.pack(side=RIGHT)

		self.update()
		self.root.mainloop()


	def update(self):
		ret, frame = self.cap.read()
		if ret:
			rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

			rotated_frame = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2RGB)
			img = Image.fromarray(rotated_frame)
			img_tk = ImageTk.PhotoImage(image=img)
			self.feed_label.img = img_tk
			self.feed_label.config(image=img_tk)
			if self.recording:
				self.video_writer.write(rotated_frame)

		self.root.after(10, self.update)

	def capture_image(self):
		ret, frame = self.cap.read()
		if ret:
			try:
				file_location = r'media/images/'
				file_name = r'captured_image_' + str(datetime.now()) + '.jpg'
				full_path = os.path.join(file_location, file_name)
				cv2.imwrite(full_path, frame)
				print(f'Image saved: {full_path}')
			except Exception as e:
				print(f'Error saving image: {e}')

	def start_recording(self):
		file_location = r'media/videos/'
		file_name = r'recorded_video.avi'
#		file_name = r'recorded_video_' + str(datetime.now()) + '.avi'
		full_path = os.path.join(file_location, file_name)
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		self.video_writer = cv2.VideoWriter(full_path, fourcc, 12.0, (640, 480))
		print(f'Recording started: {full_path}')
		self.recording = True
		self.start_button.config(state=DISABLED)
		self.stop_button.config(state=NORMAL)

	def stop_recording(self):
		print('Recording stopped')

		self.recording = False
		self.video_writer.release()

		self.start_button.config(state=NORMAL)
		self.stop_button.config(state=DISABLED)

if __name__ == "__main__":
	app = GUI_App('http://192.168.1.212/live')
