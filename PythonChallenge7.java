import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.Color;


public class PictureTester
{
    public static void main(String[] args)
    {
        String thing = "";
        BufferedImage image = null;
        
        try{
            image = ImageIO.read(new File("gradient.png"));
        }
        catch(IOException e)
        {
            System.out.println("error");
        }
        
        int w = image.getWidth();
        int h = image.getHeight();
        
        System.out.println("Image Dimension: Height-" + h + ", Width-"+ w);
        
        int total_pixels = (h * w);
        
        for(int x = 0 ; x < w; x++)
        {
                int rgb = image.getRGB(x, 1);
                Color c = new Color(rgb);
                thing += (char)(c.getRed());
                System.out.print("x: " + x + ": ");
                System.out.println(c);
        }
        
        System.out.println(thing);
        //answer: http://www.pythonchallenge.com/pc/def/integrity.html
        }
    }
