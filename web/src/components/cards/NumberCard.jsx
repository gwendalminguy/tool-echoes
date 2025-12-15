function NumberCard({ cardClass, name, dataCount, dataDuration }) {

  if (dataCount == null || dataDuration == null) return <div className={cardClass}>No Data</div>;

  return (
    <div className={`${cardClass} flex flex-col justify-between`}>
      <h2 className="text-lg font-semibold mb-4">{name}</h2>

      <div className="grid grid-cols-2 gap-5 divide-x divide-base-content/10">
        {/* Count */}
        <div className="flex flex-col">
          <span className="text-sm uppercase font-semibold opacity-50 tracking-wide">
            Titles
          </span>
          <span className="text-4xl font-bold leading-tight">
            {dataCount.toLocaleString("fr-FR")}
          </span>
        </div>

        {/* Duration */}
        <div className="flex flex-col">
          <span className="text-sm uppercase font-semibold opacity-50 tracking-wide">
            Minutes
          </span>
          <span className="text-4xl font-bold leading-tight">
            {dataDuration.toLocaleString("fr-FR")}
          </span>
        </div>
      </div>
    </div>
  );
}

export default NumberCard;
