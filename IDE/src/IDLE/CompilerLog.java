/** Instituto Tecnológico de Costa Rica
 *  Lenguajes, Compiladores e Interpretes
 *  Prof. Marco Hernandez Vasquez
 *  I Semestre, 2021
 *
 * @author Steven Badilla, Valeria Ortiz, Andrey Sanchez, Bryan Solano
 */

package IDLE;

import javax.swing.*;
import java.awt.*;

public class CompilerLog extends JPanel{

    // Definicion de los componentes del Panel
    private JTextArea taLog;
    private JPanel panel1;
    private JScrollPane scrollpane;
    private JLabel etiqueta;

    /**
     * Constructor del JPanel y todos sus componentes
     */
    public CompilerLog(){
        setLayout(new BorderLayout(0,0));

        this.setBackground(new Color(50, 56, 66));

        scrollpane = new JScrollPane();
        scrollpane.setPreferredSize(new Dimension(600,85));
        add(scrollpane, BorderLayout.SOUTH);

        etiqueta = new JLabel();
        etiqueta.setText("Event Log");
        etiqueta.setForeground(Color.WHITE);
        add(etiqueta, BorderLayout.NORTH);

        taLog = new JTextArea();
        taLog.setEnabled(true);
        taLog.setEditable(false);
        taLog.setBackground(new Color(15, 15, 15));
        scrollpane.setViewportView(taLog);

    }

    /**
     * Funcion para reemplazar el texto en el editor
     * @param texto: String a agregar en el editor
     */
    public void refresh(String texto){
        taLog.setText(texto);
        taLog.update(taLog.getGraphics());
    }

    /**
     * Funcion para cambiar el color del texto en el editor
     * @param color: Numero asociado a uno de los tres colores posibles
     */
    public void setTextColor(int color){
        if(color == 0){
            taLog.setForeground(Color.WHITE);
        }
        else if(color == 1){
            taLog.setForeground(Color.RED);
        }
        else{
            taLog.setForeground(Color.GREEN);
        }
    }
}
