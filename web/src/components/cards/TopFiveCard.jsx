function TopFiveCard({ cardClass, name, data, unit }) {

  if (!data) return <div className={cardClass}>No Data</div>;

  return (
    <div className={cardClass}>
      <h2 className="text-xl font-semibold mb-4">{name}</h2>
      <ol className="list-decimal ml-6 space-y-2">
        {data.map((item, index) => (
          <li key={index}>
            <span className="font-medium">{item.primary}</span>
            <span className="text-gray-500"> ({item.secondary} {unit})</span>
          </li>
        ))}
      </ol>
    </div>
  );
}

export default TopFiveCard;
