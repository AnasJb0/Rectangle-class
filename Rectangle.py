class Rectangle():
    _count = 0
    def __init__(self, longueur = 0, largeur = 0):
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._count += 1  
    def Getlongueur(self) :
        return self._longueur 

    def setlongueur(self, new_longueur) :
        self._longueur = new_longueur

    def Getlargeur(self) :
        return self._largeur

    def setlargeur(self, new_largeur) :
        self._largeur = new_largeur

    def Getcount(self) :
        return Rectangle._count

    def Equals(self, Rec1) :
        if self._largeur == Rec1._largeur and self._longueur == Rec1._longueur :
            return True
        else : 
            return False

    def Perimetre(self):
        P = (self._largeur + self._longueur) * 2 
        return P 

    def Surface(self) :
        return self._largeur * self._longueur

    def ToString (self) :
        return (f"Width :  {str(self.Getlargeur())} , Length : {str(self.Getlongueur())} ,  NbrRectangle : {str(self.Getcount())} .")

class Parallelepiped (Rectangle) :
    _countt = 0 
    def __init__(self, longueur = 0, largeur = 0, hauteur = 0 ):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
        Parallelepiped._countt += 1 
    def Gethauter(self) :
        return self.__hauteur  

    def sethauter(self, hauteur) :
        self.__hauteur = hauteur 

    def Getcountt(self) :
        return Parallelepiped._countt

    def Equals(self, par) :  
        if self.Getlargeur() == par.Getlargeur() and self.Getlongueur() == par.Getlongueur() and self.__hauteur == par.__hauteur :
            return True
        else : 
            return False

    def Surface(self):
        return (super().Surface() + self.__hauteur * self.Getlargeur() + self.__hauteur * self.Getlongueur())*2

    def ToString (self) :
        return (f"Width : {str(self.Getlargeur())} ,  Length :  {str(self.Getlongueur())} , height : {str(self.Getcountt())} , NbrParallelepiped : {str(self.Getcount())} .")

    def Volume (self) :
        return  self.Getlargeur() * self.Getlongueur() * self.__hauteur
