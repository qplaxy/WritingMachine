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



public class TextEditor extends JPanel {

    // Definicion de los componentes del Panel
    private JTextArea taEditor;
    private JScrollPane scrollpane;
    private TextLineNumber tln;

    /**
     * Constructor del JPanel y todos sus componentes
     */
    public TextEditor(){
        setLayout(new BorderLayout(0,0));

        scrollpane = new JScrollPane();
        add(scrollpane, BorderLayout.CENTER);

        taEditor = new JTextArea();
        scrollpane.setViewportView(taEditor);

        tln = new TextLineNumber(taEditor);
        tln.setBorderGap(-1);
        tln.setDigitAlignment(CENTER_ALIGNMENT);
        tln.setCurrentLineForeground(Color.GREEN);
        scrollpane.setRowHeaderView(tln);

    }

    /**
     * Funcion para obtener el texto escrito en el editor
     * @return texto: String con el texto escrito en el Editor
     */
    public String getTexto(){
        return taEditor.getText();
    }

    /**
     * Funcion para reemplazar el texto en el editor
     * @param texto: String a agregar en el editor
     */
    public void refresh(String texto){
        taEditor.setText(texto);
    }
}
