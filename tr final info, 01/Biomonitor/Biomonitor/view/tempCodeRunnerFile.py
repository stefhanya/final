esvio = self.__ventanaPadre._miCoordinador.generar_histograma_desviacion()
        if desvio is None:
            return

        fig, ax = plt.subplots(figsize=(2,2), dpi=100)
        ax.hist(desvio, bins=20)
        ax.set_title("Histograma de desviación")
        ax.set_xlabel("Valor")
        ax.set_ylabel("Frecuencia")
        fig.tight_layout()

        # Renderizar la figura a imagen usando Agg (igual que espectro)
        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        width, height = fig.get_size_inches() * fig.get_dpi()
        width = int(width)
        height = int(height)

        # bytesPerLine = 4 * width para RGBA
        buf = canvas.buffer_rgba()
        qimage = QImage(buf, width, height, 4 * width, QImage.Format_RGBA8888)

        pixmap = QPixmap.fromImage(qimage)
        self.desviacion.setPixmap(pixmap)

        plt.close(fig)