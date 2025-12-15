import { useState, useEffect } from "react";

function TopCard({ cardClass, name, data, unit }) {
  const [page, setPage] = useState(0);
  const pageSize = 5;

  if (!data) return <div className={cardClass}>No Data</div>;

  const pageCount = Math.ceil(data.length / pageSize);

  const startIndex = page * pageSize + 1;

  const pageData = data.slice(
    page * pageSize,
    page * pageSize + pageSize
  );

  useEffect(() => {
    setPage(0);
  }, [data]);

  return (
    <div className={`${cardClass} flex flex-col justify-between`}>
      <div className="">
        <h2 className="text-lg font-semibold mb-4">{name}</h2>

        {/* Data */}
        <ol start={startIndex} className="list-decimal ml-6 space-y-2">
          {pageData.map((item, index) => (
            <li key={page * pageSize + index}>
              <span className="font-medium">{item.primary}</span>
              <span className="text-gray-500 whitespace-nowrap"> ({item.secondary.toLocaleString("fr-FR")} {unit})</span>
            </li>
          ))}
        </ol>
      </div>

      {/* Pagination */}
      <div className="flex justify-between items-center mt-4 text-sm">
        <button disabled={page === 0} onClick={() => setPage((p) => p - 1)} className={`px-2 cursor-pointer ${page === 0 && "text-gray-400"}`}>
          ←
        </button>

        <div className="flex flex-row gap-5">
        {[...Array(pageCount)].map((_, index) => (
          <button key={index} onClick={() => setPage(index)} className={`w-3 h-3 rounded-full transition-all duration-300 cursor-pointer ${index === page ? "bg-primary" : "bg-primary/20"}`} />
        ))}
        </div>

        <button disabled={page === pageCount - 1} onClick={() => setPage((p) => p + 1)} className={`px-2 cursor-pointer ${page === pageCount - 1 && "text-gray-400"}`}>
          →
        </button>
      </div>
    </div>
  );
}

export default TopCard;
