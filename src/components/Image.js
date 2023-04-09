const Image = ({ src, width, alt, height }) => {
  return (
    <>
      <img
        src={src}
        width={width}
        height={height}
        alt={alt}
      />
    </>
  );
};

export default Image;
