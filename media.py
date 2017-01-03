import webbrowser
class Movie():
    VALID_RATINGS=["G","PG","CG","R"]
    def __init__(self,movie_title,m_Line,p_img,tr_m):
        self.title=movie_title
        self.storyLine = m_Line
        self.image = p_img
        self.trailer = tr_m
    def show_trailer(self):
        webbrowser.open(self.trailer)
        
