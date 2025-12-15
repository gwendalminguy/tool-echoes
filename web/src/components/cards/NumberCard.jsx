function NumberCard({ cardClass, name, dataCount, dataDuration }) {

  if (!dataCount || !dataDuration) return <div className={cardClass}>No Data</div>;

  return (
    <div className={cardClass}>
      <h2 className="text-lg font-semibold mb-4">{name}</h2>
      <div className="flex flex-row justify-between">
        <div className="flex flex-row items-end gap-3">
          <span className="text-4xl font-semibold">{dataCount.toLocaleString("fr-FR")}</span>
          <span className="text-xl font-semibold"> titles</span>
        </div>
        <div className="flex flex-row items-end gap-3">
          <span className="text-4xl font-semibold">{dataDuration.toLocaleString("fr-FR")}</span>
          <span className="text-xl font-semibold"> minutes</span>
        </div>
      </div>
    </div>
  );
}

export default NumberCard;
