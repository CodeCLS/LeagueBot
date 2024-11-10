module com.lol.ml.lolmloverlay {
    requires javafx.controls;
    requires javafx.fxml;
    requires opencv;
    requires java.desktop;


    opens com.lol.ml.lolmloverlay to javafx.fxml;
    exports com.lol.ml.lolmloverlay;
}